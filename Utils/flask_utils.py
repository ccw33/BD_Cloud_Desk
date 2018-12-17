# encoding:utf-8
from datetime import timedelta

from Utils.conf import Conf
from flask import request, Blueprint, session, abort,current_app


# Cross_Origin_Headers = {
#     "Access-Control-Allow-Credentials": "true",
#     'Access-Control-Allow-Origin': 'http://127.0.0.1:8080',
#     # 'Access-Control-Allow-Origin': 'http://172.16.110.19:8080'
# }


def Cross_Origin_Headers(request):
    Origin_Header = request.headers.environ['HTTP_ORIGIN']
    return {
        "Access-Control-Allow-Credentials": "true",
        'Access-Control-Allow-Origin': Origin_Header,
    }


backend_server_ip = Conf.get('BACKEND_SERVER', 'ip')
# is_local_server = backend_server_ip=='127.0.0.1' or backend_server_ip=='localhost' #本地服务器就说明是盒子版
is_local_server = True

def vm_server():
    return 'https://{0}:{1}/'.format(Conf.get('SERVER', 'ip'), Conf.get('SERVER', 'port'))


def need_set_vm_server():
    if is_local_server:
        if (not Conf.get('SERVER', 'ip')) or (not Conf.get('SERVER', 'port')):
            abort(400,"请先设置服务器地址和端口")
    else:
        session.permanent = True  # 关闭浏览器重新打开还保存session
        permanent_session_lifetime = timedelta(days=30)  # session失效时间
        if (not session['vm_server_host']) or (not session['vm_server_port']):
            abort(400,"请先设置服务器地址和端口")


dont_need_login_list = ['device.pong',]
def need_login():
    pass
    if is_local_server:
        # if Conf.get('USER','account') and 'account' in session and  session['account']==Conf.get('USER','account'):
        for item_str in dont_need_login_list:
            if not request.path.find(item_str,0,len(request.path))==-1:
                return
        if Conf.get('USER', 'account') and Conf.get('USER', 'is_login')=='true':
            need_set_vm_server()
        else:
            abort(401)
    else:
        if 'account' in session and request.cookies['account'] == session['account']:
            need_set_vm_server()
        else:
            abort(401)
