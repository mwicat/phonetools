import sys

import plac
import time

import pycisco.cmpush as cmpush
import pycisco.cmxml as cmxml

def create_set_ringer(num):
    ringer_key = 'Key:KeyPad%d' % num
    return 'Key:Settings', 'Key:KeyPad2', ringer_key, 'Key:Soft1', 'Key:Soft3', 'Key:Settings'

if __name__ == '__main__':
    ip = sys.argv[1]
    ringer = int(sys.argv[2])
    for url in create_set_ringer(ringer):
        cmpush.execute(ip, cmxml.create_execute_url(url), 'user', 'password')
        time.sleep(0.5)
