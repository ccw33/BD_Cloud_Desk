# encoding:utf-8
import threading
import re
import sys
import platform
from open import base_url
from Utils.conf import Conf

is_windows = platform.system() == 'Windows'
is_windows = True

if is_windows:
    import webview


    def close_message_listener(receiver):
        close = receiver.recv()
        if close:
            webview.destroy_window()
            print('窗口  close')


    def open_window(receiver, title, url):
        t = threading.Thread(target=close_message_listener, args=(receiver,))  # 接收关闭信号并关闭窗口的线程
        t.start()
        uid = webview.create_window(title=title, url=url)
        return uid

else:
    import htmlPy
    from PySide import QtCore, QtGui


    def close_message_listener_htmlpy(receiver, web_app):
        close = receiver.recv()
        if close:
            web_app.stop()
            print('窗口  close')


def ip_window(receiver):
    '''
    打开ip窗口并返回该对象
    :return: web_app
    '''

    if not is_windows:
        web_app = htmlPy.WebAppGUI(title=u"Python Website",
                                   width=450, height=600,
                                   developer_mode=True)
        # 禁掉右键
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            web_app.right_click_setting(htmlPy.settings.DISABLE)
        # 获取中心点坐标
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        x, y = re.findall(r'\d+', str(cp))
        # 修改窗口坐标
        web_app.x_pos = int(x) - web_app.width / 2
        web_app.y_pos = int(y) - web_app.height / 2

        # 隐藏菜单栏
        # web_app.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        web_app.url = u"%s#/" % base_url
        t = threading.Thread(target=close_message_listener_htmlpy, args=(receiver, web_app))  # 接收关闭信号并关闭窗口的线程
        t.start()
        web_app.start()
    else:
        t = threading.Thread(target=close_message_listener, args=(receiver,))  # 接收关闭信号并关闭窗口的线程
        t.start()
        uid = webview.create_window("网络设置", "%s#/" % base_url, width=450, height=600)
        return uid


def wifi_list(receiver, x_post=None, y_post=None):
    '''
    打开wifi窗口并返回该对象
    :return: web_app
    '''
    if not is_windows:
        web_app = htmlPy.WebAppGUI(title=u"Python Website",
                                   width=224, height=500,
                                   developer_mode=True)
        # 禁掉右键
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            web_app.right_click_setting(htmlPy.settings.DISABLE)
        # 获取中心点坐标
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        x, y = re.findall(r'\d+', str(cp))
        # 修改窗口坐标
        web_app.x_pos = int(x) * 2 - web_app.width - (20 if x_post == None else x_post)
        web_app.y_pos = int(y) * 2 - web_app.height - (40 if y_post == None else y_post)

        # 隐藏菜单栏
        # web_app.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        web_app.url = u"%s#/wifi" % base_url

        t = threading.Thread(target=close_message_listener_htmlpy, args=(receiver, web_app))  # 接收关闭信号并关闭窗口的线程
        t.start()
        web_app.start()
    else:
        t = threading.Thread(target=close_message_listener, args=(receiver,))  # 接收关闭信号并关闭窗口的线程
        t.start()
        uid = webview.create_window("wifi列表", "%s#/wifi" % base_url, width=224, height=500, )
        return uid


def wifi_link(receiver, append_url):
    '''
    打开wifi窗口并返回该对象
    :return: web_app
    '''
    if not is_windows:
        web_app = htmlPy.WebAppGUI(title=u"Python Website",
                                   width=450, height=250,
                                   developer_mode=True)
        # 禁掉右键
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            web_app.right_click_setting(htmlPy.settings.DISABLE)
        # 获取中心点坐标
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        x, y = re.findall(r'\d+', str(cp))
        # 修改窗口坐标
        web_app.x_pos = int(x) - web_app.width / 2
        web_app.y_pos = int(y) - web_app.height / 2

        # 隐藏菜单栏
        # web_app.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        web_app.url = u"%s%s#/wifi_connect_win" % (base_url, append_url)

        t = threading.Thread(target=close_message_listener_htmlpy, args=(receiver, web_app))  # 接收关闭信号并关闭窗口的线程
        t.start()
        web_app.start()
    else:
        t = threading.Thread(target=close_message_listener, args=(receiver,))  # 接收关闭信号并关闭窗口的线程
        t.start()
        uid = webview.create_window("连接wifi", "%s#/wifi_connect_win" % base_url, width=450, height=250)
        return uid


def screen_set(receiver):
    '''
    打开ip窗口并返回该对象
    :return: web_app
    '''

    if not is_windows:
        web_app = htmlPy.WebAppGUI(title=u"Python Website",
                                   width=370, height=280,
                                   developer_mode=True)
        # 禁掉右键
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            web_app.right_click_setting(htmlPy.settings.DISABLE)
        # 获取中心点坐标
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        x, y = re.findall(r'\d+', str(cp))
        # 修改窗口坐标
        web_app.x_pos = int(x) - web_app.width / 2
        web_app.y_pos = int(y) - web_app.height / 2

        # 隐藏菜单栏
        # web_app.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        web_app.url = u"%s#/screen_set" % base_url
        t = threading.Thread(target=close_message_listener_htmlpy, args=(receiver, web_app))  # 接收关闭信号并关闭窗口的线程
        t.start()
        web_app.start()
    else:
        t = threading.Thread(target=close_message_listener, args=(receiver,))  # 接收关闭信号并关闭窗口的线程
        t.start()
        uid = webview.create_window("分辨率设置", "%s#/screen_set" % base_url, width=370, height=280)
        return uid


def all():
    '''
    打开ip窗口并返回该对象
    :return: web_app
    '''

    if not is_windows:
        # 生产模式
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            web_app = htmlPy.WebAppGUI(title=u"Python Website", width=1440, height=838,
                                       developer_mode=True, plugins=True)
            web_app.right_click_setting(htmlPy.settings.DISABLE)
        else: # debug模式
            web_app = htmlPy.WebAppGUI(title=u"Python Website", width=1440, height=838,
                                       developer_mode=True, plugins=True)
        # # 获取中心点坐标
        # cp = QtGui.QDesktopWidget().availableGeometry().center()
        # x, y = re.findall(r'\d+', str(cp))
        # # 修改窗口坐标
        # web_app.x_pos = int(x) - web_app.width / 2
        # web_app.y_pos = int(y) - web_app.height / 2

        # # 隐藏菜单栏
        # web_app.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        web_app.url = u"http://127.0.0.1:5082/#/login"
        # web_app.url = u"http://127.0.0.1:8080/#/"
        # web_app.url = u"https://cn.vuejs.org/v2/guide/components-props.html"

        # t = threading.Thread(target=close_message_listener_htmlpy, args=(receiver, web_app))  # 接收关闭信号并关闭窗口的线程
        # t.start()
        web_app.start()
    else:
        # 生产模式
        if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
            webview.create_window("bd_desk", "http://127.0.0.1:5082/#/login",  debug=False,
                                  fullscreen=True)
        else:  # debug模式
            webview.create_window("bd_desk", "http://192.168.100.107:8080/#/login", width=1440, height=838, debug=True,
                                  fullscreen=False)



if __name__ == "__main__":
    # if sys.argv[1] == 'ip':
    #     ip_window()
    # elif sys.argv[1] == 'wifi':
    #     wifi_list()
    # elif sys.argv[1] == 'wifi_set':
    #     wifi_link()
    # else:
    all()

    # app = QApplication(sys.argv)
    # web = QWebView()
    # web.load(QUrl("https://pythonspot.com"))
    # web.show()
    #
    # sys.exit(app.exec_())