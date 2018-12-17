#encoding:utf-8
import re
import sys
import json
import logging
import multiprocessing
import threading
import traceback

import subprocess

import os

import time

import datetime
import requests
from flask import Flask, render_template, Response, request, Blueprint, session, abort, current_app
from werkzeug.exceptions import HTTPException

from app import network, windows, resolution, vm_operate
from Utils import log_utils, flask_utils, thread_utils, encryption_utils
from Utils.conf import Conf
from app import server
from vclient_python.client import Client as LocalVmClient
import random

operation_system_blueprint = Blueprint(
    'operation_system',
    __name__,
    url_prefix='/api/operation_system'
)

vclient = LocalVmClient()
# 虚机操作状态码
vm_action_status_map = {
    0: '成功',
    1: '创建错误',
    2: '下载镜像错误',
    3: '找不到虚机',
    4: '参数错误',
    5: '磁盘空间不足',
    6: '执行命令行错误',
    7: 'libvirt虚拟化层的错误',
    8: '数据库错误',
    9: '未知错误',
    10:'创建虚机磁盘镜像失败',
    11:'删除快照错误'
}


def randomUUID():
    u = [random.randint(0, 255) for ignore in range(0, 16)]
    u[6] = (u[6] & 0x0F) | (4 << 4)
    u[8] = (u[8] & 0x3F) | (2 << 6)
    return "-".join(["%02x" * 4, "%02x" * 2, "%02x" * 2, "%02x" * 2,
                     "%02x" * 6]) % tuple(u)



@operation_system_blueprint.route('/snapshot_operation/<operation>', methods=['GET'])
def snapshot_operation(operation):
    '''
    直接调用快照相关操作
    :return:
    '''
    try:
        if not re.findall(r'snapshot',operation):
            raise Exception('只允许进行snapshot操作（请求类似/snapshot_operation/.*snapshot.*）')
        data = request.args.to_dict()
        return_data = getattr(vclient,operation)(**data)
        if return_data['code']!=0:
            current_app.logger.error('{0}：{1}'.format(vm_action_status_map[return_data['code']],return_data))
            abort(500,vm_action_status_map[return_data['code']])
        return {'content':return_data['results']}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)

@operation_system_blueprint.route('/is_wifi_enabled', methods=['GET'])
def is_wifi_enabled():
    '''
    判断wifi是否开启了
    :return:{'content': 'success'}
    '''
    try:
        return {'content': json.dumps(network.is_wifi_enabled())}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/is_access_point_actived', methods=['GET'])
def is_access_point_actived():
    '''
    判断某个wifi是否连接了
    :return:{'content': 'success'}
    '''
    try:
        data = request.args.to_dict()
        return {'content': json.dumps(network.is_access_point_actived(data['ssid'], data['ap_mac']))}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/can_connect_vm_server', methods=['GET'])
def can_connect_vm_server():
    '''
    :return:{'content': 'success'}
    '''
    try:
        resp = requests.get(flask_utils.vm_server(), verify=False, timeout=5)
        # resp = requests.get('https://10.100.11.199:5445',verify=False,timeout=5)
        return {'content': 'success'}
    except requests.ConnectionError  as e:
        current_app.logger.error('无法连接虚机服务器{0}'.format(flask_utils.vm_server()))
        abort(408, '无法连接虚机服务器')
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/link_vm', methods=['GET'])
def link_vm():
    '''
    需要数据
    :return:
    '''
    # 跨域和返回数据设置
    data = request.args.to_dict()  # 需要configId, vm_name
    current_app.logger.debug(data)

    try:
        vm_status_data = server.start_spice(data['configId'])
        current_app.logger.debug("vm_status_data: %s" % vm_status_data)
        console = vm_status_data['console']

        if Conf.get('SERVER', 'ip') and Conf.get('SERVER', 'port'):
            vm_operate.spice_connect_vm(
                vm_operate.set_remote_viewer_argv(Conf.get('SERVER', 'ip'), Conf.get('SERVER', 'port'),
                                                  Conf.get('USER', 'account'), Conf.get('USER', 'password'),
                                                  console,
                                                  data['vm_name']))
            return {'content': 'success'}
        else:
            current_app.logger.error(os.path.abspath(__file__) + '还没设置ip和port')
            abort(400, '请先设置服务器ip和port')
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


# @operation_system_blueprint.route('/get_local_vm_status', methods=['GET'])
# def get_local_vm_status():
#     try:
#         data = request.args.to_dict()  # 需要configId, vm_name
#         config_id = data['configId']
#
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         current_app.logger.error(traceback.format_exc())
#         abort(500)


@operation_system_blueprint.route('/link_local_created_vm', methods=['GET'])
def link_local_created_vm():
    '''
    需要参数 configId
    :return:{'content': 'success'}
    '''
    try:
        data = request.args.to_dict()  # 需要configId, vm_name
        config_id = data['configId']
        t = threading.Thread(target=vclient.start, args=(config_id,))
        t.start()
        return {'content': 'success'}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/link_local_vm', methods=['GET'])
def link_local_vm():
    try:
        data = request.args.to_dict()  # 需要configId, vm_name
        current_app.logger.debug(data)
        config_id = data['configId']
        image_id = data['image_id']

        image_size = data['image_size']
        cpu = data['cpu']
        ram = data['ram']
        volume_size = data['volume_size']
        os_type = data['os_type']
        name = data['name']

        def create_locl_vm():
            print('################## in thread')
            state = vclient.create(config_id,
                                   cpu,
                                   ram,
                                   image_id,
                                   os_type,
                                   image_size,
                                   volume_size,
                                   name,
                                   Conf.get('SERVER', 'ip'),
                                   Conf.get('SERVER', 'port'),
                                   Conf.get('USER', 'account'),
                                   Conf.get('USER', 'password'))['results']['state']
            print('################## create in thread')
            # {
            #     'building': '虚机正在创建中',
            #     'downloading_image': '正在下载镜像',
            #     'download_completed': '下载镜像完成',
            #     'builded': '虚机已创建',
            #     'active': '虚机活动中,请切换到虚机',
            #     'shutdown': '虚机在关机状态',
            #     'error': '创建虚机出现错误',
            # }
            print('################## vm state：{0}'.format(state))

            while True:
                time.sleep(2)
                vm_status = vclient.get_status(config_id)
                if vm_status['code'] == 0:
                    if vm_status['results'] in ['builded', 'shutdown', 'active']:
                        vclient.start(config_id)
                        break
                    else:
                        pass
                else:
                    abort(500, vm_action_status_map[vm_status['code']])

        t = threading.Thread(target=create_locl_vm)
        t.start()

        # def test():
        #     time.sleep(20)
        #     print('############################ thread_test')
        # t = threading.Thread(target=test,)
        # t.start()
        return {'content': 'success'}

    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/stop_vm', methods=['GET'])
def stop_vm():
    '''
    需要参数
    :return:{'content': 'success'}
    '''
    try:
        def stop_all():
            # 关闭所有本地的虚机
            config_id_list = [item['id'] for item in vclient.list()['results']]
            for config_id in config_id_list:
                vm_status = vclient.get_status(config_id)
                if vm_status['results'] == 'active':
                    vclient.stop(config_id)
            # 关闭所有虚机服务器的虚机
            p = subprocess.Popen('killall -9 remote-viewer', shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            (stdoutput, erroutput) = p.communicate()

        t = threading.Thread(target=stop_all)
        t.start()
        return {'content': 'success'}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_local_vm_status', methods=['GET'])
def get_local_vm_status():
    try:
        data = request.args.to_dict()  # 需要configId

        config_id = data['configId']

        # vclient = LocalVmClient()
        # 获取虚机状态
        vm_status = vclient.get_status(config_id)
        # vm_current_status_map = {
        #     'building': '虚机正在创建中',
        #     'downloading_image': '正在下载镜像',
        #     'download_completed': '下载镜像完成',
        #     'builded': '虚机已创建',
        #     'active': '虚机活动中',
        #     'shutdown': '虚机在关机状态',
        #     'error': '创建虚机出现错误',
        #     None: '虚机创建出现错误'  #暂时没叼用
        # }
        print(vm_status)

        if vm_status['code'] == 0:
            return {'content': vm_status['results']}
        else:
            return {'content': vm_action_status_map[vm_status['code']]}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_created_local_vms')
def get_created_local_vms():
    '''
    获取本地已创建虚机
    :return:
    '''
    try:
        # vclient = LocalVmClient()
        local_created_vms = vclient.list()['results']
        return {'content': local_created_vms}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_current_mac')
def get_current_mac():
    '''
    当前连接虚机服务器的mac
    :return:
    '''
    try:
        p = subprocess.Popen("ip route get {0}".format(Conf.get('SERVER', 'ip')), shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        (stdoutput, erroutput) = p.communicate()
        dev_name = re.findall(r'dev (.+?(?= )) ', stdoutput.decode())[0]
        p = subprocess.Popen("ip link show dev {0}".format(dev_name), shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        (stdoutput, erroutput) = p.communicate()
        current_mac = re.findall(r'link/ether (.+?(?= ))', stdoutput.decode())[0]
        return {'content': current_mac}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_all_mac_str')
def get_all_mac_str():
    '''
    获取本地已创建虚机
    :return:
    '''
    try:
        all_mac = network.get_all_mac()
        all_mac_text = ''.join(all_mac)
        return_text = encryption_utils.bd_crypt.encrypt(all_mac_text).decode()
        return {'content': return_text}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_lans')
def get_lans_data():
    try:
        # # 跨域和返回数据设置
        # info = [
        #     {
        #         'lan': '111',
        #         'is_auto': True,
        #         'isActive':True,
        #         'ip': '172.10.1.2',
        #         'subnet_mask': '125.214.12.0',
        #         'gateway': '158.158.12.1',
        #         'dns': '15.125.67.25',
        #         'mac': 'EC:D6:8A:1C:B2:D4',
        #         'id': "net1"
        #     },
        #     {
        #         'lan': '222',
        #         'is_auto': False,
        #         'isActive': False,
        #         'ip': '172.10.1.33',
        #         'subnet_mask': '125.214.12.0',
        #         'gateway': '158.158.12.1',
        #         'dns': '114.114.114.114',
        #         'mac': 'EC:D6:8A:1C:HH:D5',
        #         'id': "net2"
        #     },
        # ]
        # resp = Response(json.dumps(info), mimetype='application/json')

        net_info = network.getNetworkInfo()
        for index, info in enumerate(net_info):
            if index == 0:
                net_info[index]['isActive'] = True
                continue
            net_info[index]['isActive'] = False
        current_app.logger.error("get_lans_data %s" % net_info)
        return {
            'errorInfo': 'success',
            'result': net_info
        }
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/save_lan', methods=['POST'])
def save_lan():
    # 跨域和返回数据设置
    data = request.form.to_dict()
    try:
        if data['is_auto'] == 'true':
            network.setDHCP(data['lan'], int(data['type']))
        else:
            network.setNetwork(data['lan'], data['mac'], data['ip'], data['subnet_mask'], data['gateway'], data['dns'],
                               int(data['type']))
        return {'content': 'success'}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_wifis')
def get_wifis():
    try:
        wifi_list = network.getWifiList()['wifi_list']

        wifi_pwd = {}
        with open('file/wifi_pwd', 'r') as fr:
            text = fr.read()
            if text:
                wifi_pwd = json.loads(text)
        remembered_pass_keys = wifi_pwd.keys()

        for index, wifi in enumerate(wifi_list):
            wifi_list[index]['strength'] = 4 - (wifi_list[index]['strength'] * 4 / 100) - 1
            if wifi['name'] in remembered_pass_keys:
                wifi['password'] = wifi_pwd[wifi['name']]
                wifi['remember_pwd'] = True
        return wifi_list
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/connect_wifi', methods=['POST'])
def connect_wifi():
    try:
        data = request.form.to_dict()
        network.connectWifi(
            data['name'], data['is_lock'],
            data['password'], device_name=data["interface_name"])
        wifi_pwd = {}
        with open('file/wifi_pwd', 'r') as fr:
            text = fr.read()
            if text:
                wifi_pwd = json.loads(text)
        with open('file/wifi_pwd', 'w') as fw:
            if data.get('remember_pwd', None) == 'true':
                wifi_pwd[data['name']] = data['password']
            else:
                if data['name'] in wifi_pwd:
                    del wifi_pwd[data['name']]
            json.dump(wifi_pwd, fw)
        return {'content': 'success'}
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/disconnect_wifi', methods=['POST'])
def disconnect_wifi():
    try:
        data = request.form.to_dict()
        return {'content': network.disconnect_wifi(data['name'], data['interface_name'])}
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/get_resolution', methods=['GET'])
def get_resolution():
    # data = request.form.to_dict()
    try:
        resolution_list = resolution.get_resolution()

        current_app.logger.debug("get_resolution: %s" % resolution_list)
        return {
            "errorInfo": "success",
            "result": resolution_list
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/set_resolution', methods=['POST'])
def set_resolution():
    try:
        data = request.form.to_dict()

        resolution_list = resolution.set_resolution(data['selected'])

        return {'content': 'success'}
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@operation_system_blueprint.route('/shutdown', methods=['GET'])
def shutdown():
    try:
        if subprocess.call('halt'.split(' ')) == -1:
            raise Exception('关机失败')
        return {'content': '成功'}
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)

# @operation_system_blueprint.route('/open_wifi_setting', methods=['POST'])
# def open_wifi_window():
#     try:
#         data = request.form.to_dict()
#         append_url = '?'
#         for k, v in data.items():
#             append_url = append_url + k + '=' + v + '&'
#         # 查看是否已经记录密码，如果已经记录则把password=dsfew&remember_pwd=true加进去
#         wifi_pwd = {}
#         with open('file/wifi_pwd', 'r') as fr:
#             text = fr.read()
#             if text:
#                 wifi_pwd = json.loads(text)
#         if data['name'] in wifi_pwd:
#             append_url = "%spassword=%s&remember_pwd=true" % (append_url, wifi_pwd[data['name']])
#         wifi_list_sender.send(True)  # 关闭wifi_list
#         p = multiprocessing.Process(target=windows.wifi_link, args=(wifi_link_receiver, append_url))
#         p.start()
#     except Exception  as e:
#         current_app.logger.error(traceback.format_exc())
#     return ''
