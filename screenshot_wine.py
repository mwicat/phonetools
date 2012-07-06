import plac
import time

import pycisco.cmpush as cmpush
import pycisco.cmxml as cmxml

from tempfile import NamedTemporaryFile, mktemp
import os
import sys
from subprocess import call, check_output, PIPE

def win_path(path):
    return check_output(['winepath', '-w', path]).strip()

IMAGE_DIRECTORY = 'tmp'

ip = sys.argv[1]

cip_data = cmpush.screenshot(ip, 'user', 'password')

intmp = NamedTemporaryFile(delete=False)
intmp.write(cip_data)
intmp.close()

out_name = mktemp()

call(['wine', 'cip2gif.exe', win_path(intmp.name), win_path(out_name)], stdout=PIPE)

gif_file = open(out_name)

sys.stdout.write(gif_file.read())

os.unlink(intmp.name)
os.unlink(out_name)
