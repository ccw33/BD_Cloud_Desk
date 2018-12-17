#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import platform
from multiprocessing import cpu_count

def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

def get_system_type():
    system_type = platform.system()
    if system_type == 'Linux':
        return 2,system_type
    elif system_type == 'Windows':
        return 3, system_type
    else:
        return 0, None

def get_cpu_count():
    return cpu_count()

if __name__ == '__main__':
    print(get_mac_address())
    print(get_system_type())
    print('cpu_count:' + str(get_cpu_count()))