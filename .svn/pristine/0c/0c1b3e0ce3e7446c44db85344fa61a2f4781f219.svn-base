# encoding:utf-8

import json
import logging
import traceback
from datetime import timedelta

from flask import Response, request, Blueprint, session, abort,current_app
from werkzeug.exceptions import HTTPException

import requests
from Utils import log_utils, flask_utils
from Utils.conf import Conf

# logger = log_utils.Log('log/cloud_dashboard_end', level=logging.DEBUG if Conf.get('BACKEND_SERVER','mode') == 'debug' else logging.ERROR,
#                        name=__name__).logger


other_operation_blueprint = Blueprint(
    'other_operation',
    __name__,
    url_prefix='/api/other_operation'
)

# @other_operation_blueprint.before_request
# def before_request():
#     if 'account' in session and request.cookies['account'] == session['account']:
#         pass
#     else:
#         resp = Response(json.dumps({'content': '未登录'}), mimetype='application/json', status=401)
#         abort(resp)
    

@other_operation_blueprint.route('/set_vm_server', methods=['GET'])
def set_vm_server():
    '''
    设置服务器
    :return:
    '''
    try:
        data=request.args
        if flask_utils.is_local_server:
            Conf.set('SERVER', 'ip', data['vm_server_host'])
            Conf.set('SERVER', 'port', data['vm_server_port'])
        else:
            session['vm_server_host'] = data['vm_server_host']
            session['vm_server_port'] = data['vm_server_port']
        return '设置默认虚机服务器成功'
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)

@other_operation_blueprint.route('/get_vm_server', methods=['GET'])
def get_vm_server():
    '''
    设置服务器
    :return:
    '''
    try:
        data={}
        if flask_utils.is_local_server:
            data['vm_server_host'] = Conf.get('SERVER', 'ip')
            data['vm_server_port'] = Conf.get('SERVER', 'port')
        else:
            data['vm_server_host'] = session['vm_server_host']
            data['vm_server_port'] = session['vm_server_port']
        return data
    except HTTPException as e:
        raise e
    except Exception  as e:
        current_app.logger.error(traceback.format_exc())
        abort(500)