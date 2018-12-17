#encoding:utf-8
import sys
import requests
from Utils.conf import Conf

base_url = 'http://%s:%s/' % (Conf.get('BACKEND_SERVER','IP'),Conf.get('BACKEND_SERVER','PORT'))

if __name__=="__main__":
    if sys.argv[1] == 'ip':
        requests.post(base_url + 'open_ip_setting')
    elif sys.argv[1] == 'wifi':
        requests.post(base_url +(("open_wifi_list?x=%s&y=%s" % (sys.argv[2],sys.argv[3])) if len(sys.argv)>2 else 'open_wifi_list'))
    elif sys.argv[1] == 'wifi_set':
        requests.post(base_url + 'open_wifi_setting')
    elif sys.argv[1] == 'screen_set':
        requests.post(base_url + 'open_screen_setting')

