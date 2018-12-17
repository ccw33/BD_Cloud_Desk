#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pycurl
# from urllib import urlencode
# from StringIO import StringIO
# import time

import requests

from . import dev_info
import json
from Utils import flask_utils
from Utils.conf import Conf


# def get_curl(url, data):
#     postfields = urlencode(data)
#     print(url + postfields)
#     buf = StringIO()
#     curl = pycurl.Curl()
#     curl.setopt(pycurl.URL, url)
#     curl.setopt(pycurl.POSTFIELDS, postfields)
#     curl.setopt(pycurl.CUSTOMREQUEST, 'POST')
#     curl.setopt(pycurl.WRITEDATA, buf)
#     curl.setopt(pycurl.TIMEOUT, 1)
#     curl.setopt(pycurl.SSL_VERIFYHOST, 0)
#     curl.setopt(pycurl.SSL_VERIFYPEER, 0)
#     try:
#         curl.perform()
#     except pycurl.error as e:
#         print(e.args[0])
#         return None
#     curl.close()
#     #print(buf.getvalue())
#     return buf.getvalue()
#
# def multiple_get_curl(url, data ,num = 1):
#     buf = get_curl(url, data)
#     print(num)
#     if num < 1 or buf != None:
#         if num < 1:
#             return None
#         return json.loads(buf)
#     num = num - 1
#     time.sleep(1)
#     multiple_get_curl(url, data, num)
#
# def heartbeat(deviceStatus = 0):
#     url = 'https://%s:%s/api/device/pong?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     data_dict['systemName'] = dev_info.get_system_type()[1]
#     data_dict['deviceStatus'] = deviceStatus
#     return multiple_get_curl(url,data_dict, 1);
#
# def login(username, password, dynamicPassword = None):
#     url = 'https://%s:%s/api/login?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     #data_dict['systemName'] = dev_info.get_system_type()[1]
#     data_dict['dynamicPassword'] = dynamicPassword
#     return multiple_get_curl(url,data_dict, 1);
#
# def get_vm_list():
#     url = 'https://%s:%s/api/list?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     data_dict['offset'] = 0
#     data_dict['limit'] = 0
#     return multiple_get_curl(url,data_dict, 1);
#
#
#
#
#     # return multiple_get_curl(url,data_dict, 1);
#
#
# def start_vnc_or_rdp(configId = 0):
#     url = 'https://%s:%s/api/RemoteDesktopConsole?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     #data_dict['systemName'] = dev_info.get_system_type()[1]
#     data_dict['configId'] = configId
#     return multiple_get_curl(url,data_dict, 1);
#
#
# def change_password(newPassword, rePassword):
#     url = 'https://%s:%s/api/EditPassword?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     data_dict['newPassword'] = newPassword
#     data_dict['rePassword'] = rePassword
#     return multiple_get_curl(url,data_dict, 1);
#
# def get_dynamic_status():
#     url = 'https://%s:%s/api/GetDynamicPassword?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     return multiple_get_curl(url,data_dict, 1);
#
# def operate_vm(configId = 0, operate = 0):
#     url = 'https://%s:%s/api/ConsoleOperate?' % (Conf.get('SERVER','ip'), Conf.get('SERVER','port'))
#     data_dict = {}
#     if flask_utils.is_local_server:
#         data_dict['account'] = Conf.get('USER', 'account')
#         data_dict['password'] = Conf.get('USER', 'password')
#     else:
#         data_dict['account'] = session['account']
#         data_dict['password'] = session['password']
#     data_dict['mac'] = dev_info.get_mac_address()
#     data_dict['systemType'] = dev_info.get_system_type()[0]
#     data_dict['configId'] = configId
#     data_dict['operate'] = operate
#     return multiple_get_curl(url,data_dict, 1)

def start_spice(configId = 0):
    data_dict = {}
    data_dict['account'] = Conf.get('USER', 'account')
    data_dict['password'] = Conf.get('USER', 'password')
    data_dict['mac'] = dev_info.get_mac_address()
    data_dict['systemType'] = dev_info.get_system_type()[0]
    #data_dict['systemName'] = dev_info.get_system_type()[1]
    data_dict['configId'] = configId
    response = requests.get('{0}{1}'.format(flask_utils.vm_server(), 'api/ServerSPICEConsole'), data_dict, verify=False)
    if response.status_code==200:
        content = json.loads(response.content.decode())
        if content['status']== 'ACTIVE':
            return content
    raise Exception('status:%s,%s' % (content['status'],content['status_zh']))

if __name__ == '__main__':
    # print(heartbeat(1))
    # print(login())
    # print(get_vm_list())
    # print(start_vnc_or_rdp(160))
    # print(change_password('123qwe', '123qwe'))
    # print(get_dynamic_status())
    # #print(operate_vm(160, 2))
    # #print(multiple_get_curl('https://10.100.11.199:444/api/list?', {'account':'zw','password':'123qwe','mac':'74-D4-35-7C-20-0A','systemType':'2','offset':'0','limit':'0'}, 10))

    print(start_spice(160))
