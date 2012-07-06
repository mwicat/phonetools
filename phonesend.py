#x!/usr/bin/env python

from argh import *

import requests
import sys

import pycisco.cmpush as cmpush
import pycisco.cmxml as cmxml


@arg('ip')
def status(args):
    data = ''
    text = sys.stdin.read()
    push_xml = cmxml.PHONE_STATUS % {'text': text, 'width': 100, 'height': 20, 'data': data}
    cmpush.execute(args.ip, push_xml, 'user', 'password')

@arg('ip')
@arg('url')
def url(args):
    push_xml = cmxml.create_execute_url(args.url)
    cmpush.execute(args.ip, push_xml, 'user', 'password')

@arg('ip')
def raw(args):
    text = sys.stdin.read()
    cmpush.execute(args.ip, text, 'user', 'password')

def main():
    p = ArghParser()
    p.add_commands([status, url, raw])
    p.dispatch()


if __name__ == '__main__':
    main()

        
