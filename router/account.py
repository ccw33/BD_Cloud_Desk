#encoding:utf-8
import json
import logging
import traceback
from datetime import timedelta

from flask import Response, request, Blueprint, session, abort,current_app
from werkzeug.exceptions import HTTPException

import requests
from Utils import log_utils, flask_utils
from Utils.conf import Conf

# logger = log_utils.Log('log/cloud_dashboard_end',
#                        level=logging.DEBUG if Conf.get('BACKEND_SERVER', 'mode') == 'debug' else logging.ERROR,
#                        name=__name__).logger


account_blueprint = Blueprint(
    'account',
    __name__,
    url_prefix='/api/account'
)


@account_blueprint.before_request
def before_request():
    flask_utils.need_set_vm_server()



@account_blueprint.route('/login', methods=['GET'])
def login():
    try:
        path = 'api/login'
        query_string = request.query_string.decode()
        response = requests.get('{0}/{1}?{2}'.format(flask_utils.vm_server(), path, query_string), verify=False)
        if not response.status_code == 200:
            raise Exception(str(response.status_code) + ':' + response.json()['errorinfo'])

        if response.json()['errorinfo'] == 'success':
            resp = Response(json.dumps({'content': response.json()['errorinfo']}), mimetype='application/json',
                            status=200)
            if flask_utils.is_local_server:
                Conf.set('USER', 'account', request.args.to_dict()['account'])
                Conf.set('USER', 'password', request.args.to_dict()['password'])
                Conf.set('USER', 'dynamicPass', request.args.to_dict()['dynamicPass'])
                Conf.set('USER', 'remember_pass', request.args.to_dict()['remember_pass'])
                Conf.set('USER', 'auto_login', request.args.to_dict()['auto_login'])
                Conf.set('USER', 'is_login', 'true')
                # session.permanent=False
                # session['account'] = request.args.to_dict()['account']
            else:
                session['account'] = request.args.to_dict()['account']
                session['password'] = request.args.to_dict()['password']
                session['dynamicPass'] = request.args.to_dict()['dynamicPass']
                session['remember_pass'] = request.args.to_dict()['remember_pass']
                session['auto_login'] = request.args.to_dict()['auto_login']
                if request.args.to_dict()['remember_pass'] == 'false':
                    resp.set_cookie('account', request.args.to_dict()['account'])
                if request.args.to_dict()['remember_pass'] == 'true':
                    resp.set_cookie('account', request.args.to_dict()['account'], 3600 * 24 * 30)  # 如果记住密码，则保存一个月
            resp.headers.extend(flask_utils.Cross_Origin_Headers(request))
            return resp
        else:
            abort(400,response.json()['errorinfo'])
    except HTTPException as e:
        raise e
    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@account_blueprint.route('/logout', methods=['GET'])
def logout():
    try:
        resp = Response(json.dumps({'content': '登出成功'}), mimetype='application/json', status=200)
        if flask_utils.is_local_server:
            # Conf.set('USER', 'account', '')
            # Conf.set('USER', 'password', '')
            # Conf.set('USER', 'dynamicPass', '')
            # Conf.set('USER', 'remember_pass', '')
            # Conf.set('USER', 'auto_login', 'false')
            Conf.set('USER', 'is_login', 'false')
            # session.pop('account', None)
        else:
            session.pop('account', None)
            session.pop('password', None)
            session.pop('dynamicPass', None)
            session.pop('remember_pass', None)
            session.pop('auto_login', None)
            resp.set_cookie('account', '')
        resp.headers.extend(flask_utils.Cross_Origin_Headers(request))
        return resp
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)



@account_blueprint.route('/is_dynamic', methods=['GET'])
def is_dynamic():
    try:
        path = 'api/GetDynamicPassword'
        response = requests.get('{0}{1}'.format(flask_utils.vm_server(), path), verify=False)
        if response.status_code == 200:
            return {'content': response.json()['status']}
        else:
            raise Exception(response.status_code + ' api/GetDynamicPassword 失败')
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)



@account_blueprint.route('/get_ready_data', methods=['GET'])
def get_ready_data():
    '''
    登录前获取记住的账号信息以便自动填写
    :return:
    '''
    try:
        data = {}
        if flask_utils.is_local_server:
            if Conf.get('USER', 'account'):
                data['account'] = Conf.get('USER', 'account')
                data['password'] = Conf.get('USER', 'password')
                data['remember_pass'] = Conf.get('USER', 'remember_pass')
                data['auto_login'] = Conf.get('USER', 'auto_login')
                return {'content': data}
            else:
                return {'content': 'not_ready'}
        else:
            if 'account' in session and request.cookies['account'] == session['account']:
                data['account'] = session['account']
                data['password'] = session['password']
                data['remember_pass'] = session['remember_pass']
                data['auto_login'] = session['auto_login']
                return {'content': data}
            else:
                return {'content': 'not_ready'}
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)


@account_blueprint.route('/set_default_vm', methods=['GET'])
def set_default_vm():
    '''
    登录前获取记住的账号信息以便自动填写
    :return:
    '''
    try:
        data = request.args
        if flask_utils.is_local_server:
            Conf.set('VMS', 'default_vm', data['default_vm'])
            resp = Response('设置默认虚机成功', status=200)
        else:
            session['default_vm'] = data['default_vm']
            resp = Response('设置默认虚机成功', status=200)
            resp.set_cookie('default_vm', data['default_vm'], 3600 * 24 * 30)
            resp.set_cookie('default_vm_name', data['default_vm_name'], 3600 * 24 * 30)
        resp.headers.extend(flask_utils.Cross_Origin_Headers(request))
        return resp
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500, '设置默认虚机失败')

@account_blueprint.route('/is_login', methods=['GET'])
def is_login():
    '''
    登录前获取记住的账号信息以便自动填写
    :return:
    '''
    try:
        if Conf.get('USER','is_login')=='false':
            return {'content':False}
        else:
            return {'content':{
                'account':Conf.get('USER','account'),
                'password': Conf.get('USER', 'password')
            }}
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500, '设置默认虚机失败')