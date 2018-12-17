# encoding:utf-8
import threading
import re
from Utils.conf import Conf

import webview

def all():
    '''
    打开ip窗口并返回该对象
    :return: web_app
    '''

    # 生产模式
    if not Conf.get('BACKEND_SERVER', 'mode') == 'debug':
        webview.create_window("bd_desk", "http://127.0.0.1:5082/#/login",  debug=False,
                              fullscreen=False)
    else:  # debug模式
        # webview.create_window("bd_desk", "http://127.0.0.1:5082/#/login",  debug=False,fullscreen=False)
        webview.create_window("bd_desk", "http://192.168.100.110:8080/#/snapshot", width=1440, height=838, debug=True,
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
