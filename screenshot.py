import plac
import sys

import pycisco.cipimage as cipimage
import pycisco.cmpush as cmpush


from xml.etree.ElementTree import ElementTree, fromstring


ip = sys.argv[1]

cip_data = cmpush.screenshot(ip, 'user', 'password')

tree = fromstring(cip_data)

im = cipimage.load_cip(tree)

im.save(sys.stdout, format= 'JPEG')

im.show()
