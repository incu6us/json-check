#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Vyacheslav Pryimak'

version = '1.0'

from lib.jsonParse import JsonCheck
import argparse

result = list()

parse = argparse.ArgumentParser(description='JSON Check\nVersion:'+version)
parse.add_argument('-u', '--url', help='Full address to check')
parse.add_argument('-k', '--key', type=str, help='Put the key to check a value. Can be used some keys: "testkey1 testkey2"')
parse.add_argument('-e', '--exist', help='Return true if exist, else - false')
parse.add_argument('-n', '--notexist', help='Return true if not exist, else - false')

args = parse.parse_args()

if args.url != None and args.key != None and args.exist == None and args.notexist == None:
    jsonCheck = JsonCheck(url=args.url)
    for key in list(args.key.split(" ")):
        result = jsonCheck.getValue(key=key)
        print result

elif args.url != None and args.key != None and args.exist != None and args.notexist == None:
    jsonCheck = JsonCheck(url=args.url)
    for key in list(args.key.split(" ")):
        result.append(jsonCheck.getValue(key=key))
    if args.exist in result:
        print True
    else:
        print False

elif args.url != None and args.key != None and args.exist == None and args.notexist != None:
    jsonCheck = JsonCheck(url=args.url)
    for key in list(args.key.split(" ")):
        result.append(jsonCheck.getValue(key=key))
    if args.notexist not in result:
        print True
    else:
        print False