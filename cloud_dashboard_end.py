# encoding:utf-8
import json
import logging
from datetime import timedelta
from app import windows

from router import blueprints

from flask import Flask, render_template, session, request, Response, abort, jsonify
from Utils import log_utils
from Utils import flask_utils
from Utils.conf import Conf

import logging
from logging.handlers import RotatingFileHandler
import multiprocessing


# 初始化config.ini的某些配置
Conf.set('USER', 'is_login', 'false')

app = Flask(__name__, static_folder='Front/dist/static', template_folder='Front/dist')
app.secret_key = '123456'
app.config.update(
    DEBUG=True if Conf.get('BACKEND_SERVER', 'mode') == 'debug' else False,
    # PERMANENT_SESSION_LIFETIME=timedelta(days=30),
    SESSION_PERMANENT=False,
    SESSION_COOKIE_PATH='/',
    # SESSION_COOKIE_NAME='ccw_test'
)

# 解决jinja和vue的冲突
app.jinja_env.variable_start_string = '#{ '
app.jinja_env.variable_end_string = ' }#'

# 日志
# 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
rHandler = RotatingFileHandler('log/log', maxBytes=1 * 1024 * 1024, backupCount=3, encoding='utf-8')
# rHandler = logging.FileHandler(file_path, encoding='utf-8')
rHandler.setLevel(logging.DEBUG if Conf.get('BACKEND_SERVER', 'mode') == 'debug' else logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)
app.logger.addHandler(rHandler)

app_logger = app.logger


# app.logger.error(u'出错了')


class MyResponse(Response):
    '''
    自定义默认response
    '''

    def __init__(self, response, **kwargs):
        # 添加跨域响应头
        if 'HTTP_ORIGIN' in request.headers.environ:
            kwargs['headers'] = flask_utils.Cross_Origin_Headers(request)
        super(MyResponse, self).__init__(response, **kwargs)

    @classmethod
    def force_type(cls, rv, environ=None):
        '''
        自动转换响应类型
        :param rv:
        :param environ:
        :return:
        '''
        # app_logger.debug("MyResponse %s" % isinstance(rv, list))
        if isinstance(rv, dict) or isinstance(rv, list) or isinstance(rv, tuple):
            # 将dict转换为json（同时设置请求头）
            rv = jsonify(rv)
        return super(MyResponse, cls).force_type(rv, environ)


app.response_class = MyResponse


@app.errorhandler(400)
def error(e):
    default_content = (
        'The browser (or proxy) sent a request that this server could '
        'not understand.'
    )
    return {'content': e.description if e.description != default_content else '操作有误'}, 400


@app.errorhandler(408)
def error(e):
    default_content = (
        'The server closed the network connection because the browser '
        'didn\'t finish the request within the specified time.'
    )
    return {'content': e.description if e.description != default_content else '请求超时'}, 408


@app.errorhandler(500)
def error(e):
    default_content = (
        'The server encountered an internal error and was unable to '
        'complete your request.  Either the server is overloaded or there '
        'is an error in the application.'
    )
    return {'content': e.description if e.description != default_content else '服务器发生错误，请联系管理员'}, 500


@app.errorhandler(401)
def error(e):
    default_content = (
        'The server could not verify that you are authorized to access '
        'the URL requested.  You either supplied the wrong credentials (e.g. '
        'a bad password), or your browser doesn\'t understand how to supply '
        'the credentials required.'
    )
    return {'content': e.description if e.description != default_content else '未登录'}, 401


@app.errorhandler(404)
def error(e):
    default_content = (
        'The requested URL was not found on the server.  '
        'If you entered the URL manually please check your spelling and '
        'try again.'
    )
    return {'content': e.description if e.description != default_content else '找不到资源'}, 404


@app.route('/')
def hello_world():
    return render_template('index.html')


# 注册模块
for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    # 生产模式
    if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
        p = multiprocessing.Process(target=lambda : app.run(host='0.0.0.0', port=int(Conf.get('BACKEND_SERVER', 'PORT')), threaded=False))
        p.start()
        # app.run(host='0.0.0.0', port=int(Conf.get('BACKEND_SERVER', 'PORT')), threaded=False)
        windows.all()
        # p.join()
    else:  # debug模式
        app.run(host='0.0.0.0', port=int(Conf.get('BACKEND_SERVER', 'PORT')), threaded=False)
