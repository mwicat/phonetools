import Image
import ImageOps

import pycisco.cipimage as cipimage
import pycisco.cmxml as cmxml

WIDTH = 132
HEIGHT = 64

if __name__ == '__main__':
    import sys

    fname = sys.argv[1]
    outfname = sys.argv[2]

    im = Image.open(fname)

    #im = im.resize((WIDTH, HEIGHT))

    im_l = im.convert('L')

    im_post = ImageOps.posterize(im_l, 2)

    im_post.show()

    data = dump_cip(im_post)

    width, height = im_l.size

    outf = open(outfname, 'w')
    
    xml = cmxml.PHONE_IMAGE % {'width': width, 'height': height, 'data': data}
    outf.write(xml)
