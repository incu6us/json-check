# -*- coding: utf-8 -*-
__author__ = 'Vyacheslav Pryimak'

import sys
import json
import urllib2
from urllib2 import URLError


class JsonCheck:
    __url = None
    __jsonResponse = None

    def __init__(self, url=None):
        self.__url = url
        self.__connect()


    def __connect(self):
        try:
            req = urllib2.Request(self.__url, None, {'user-agent': 'json-check'})
            browse = urllib2.build_opener()
            response = browse.open(req)
            self.__jsonResponse = json.load(response)
        except URLError:
            print "Name or service not known: " + self.__url


    def getValue(self, key):
        try:
            value = self.__jsonResponse[key]
            return value
        except KeyError:
            return "Error: no data for key " + key
        except:
            return "Script exit with fail!!!"
