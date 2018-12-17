# -*- coding:utf-8 -*-
# author: ccw

# ---------------------
import sys, os
from configparser import ConfigParser


# class Db_Connector:
#     def __init__(self, config_file_path):
#         cf = ConfigParser.ConfigParser()
#         cf.read(config_file_path)
#
#         s = cf.sections()
#         print 'section:', s
#
#         o = cf.options("baseconf")
#         print 'options:', o
#
#         v = cf.items("baseconf")
#         print 'db:', v
#
#         db_host = cf.get("baseconf", "host")
#         db_port = cf.getint("baseconf", "port")
#         db_user = cf.get("baseconf", "user")
#         db_pwd = cf.get("baseconf", "password")
#
#         print db_host, db_port, db_user, db_pwd
#
#         cf.set("baseconf", "db_pass", "123456")
#         cf.write(open("config_file_path", "w"))
#
#
# if __name__ == "__main__":
#     f = Db_Connector("../config.ini")

class ConfigClass:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        self.cf.read(self.path)
        result = self.cf.get(field, key)
        return result

    def set(self, field, key, value):
        self.cf.set(field, key, value)
        self.cf.write(open(self.path,'w'))
        return True


Conf = ConfigClass('{0}/config.ini'.format(os.getcwd()))
# print Conf.get('BACKEND_SERVER','IP')
# Conf.set('baseconf','db_pass','sdfewfe')

