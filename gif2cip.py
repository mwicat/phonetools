import pycisco.cipimage as cipimage
import pycisco.cmxml as cmxml

if __name__ == '__main__':
    import sys

    fname = sys.argv[1]

    im = Image.open(fname)

    data = dump_cip(im)
    width, height = im.size
    print cmxml.PHONE_IMAGE % {'width': width, 'height': height, 'data': data}

