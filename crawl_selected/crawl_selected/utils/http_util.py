# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json

class HttpUtils(object):

    @classmethod
    def getUrl(cls,url):
        request = urllib.request.Request(url=url, headers={"Content-Type": "application/json", "Accept": "application/json"})
        jsonData = None
        with urllib.request.urlopen(request) as f:
            jsonData = json.loads(f.read().decode("utf-8"))
        return jsonData

    @classmethod
    def postJsonQuery(cls,url,query):
        queryPostString = json.dumps(query, ensure_ascii=False)
        data = bytes(queryPostString, 'utf8')
        request = urllib.request.Request(url, data, {"Content-Type": "application/json", "Accept": "application/json"})
        jsonData = None
        with urllib.request.urlopen(request) as f:
            jsonData = json.loads(f.read().decode("utf-8"))
        return jsonData

    @classmethod
    def postQuery(cls, url, params):
        data = urllib.parse.urlencode(params)
        data = data.encode('utf-8')
        request = urllib.request.Request(url)
        result = None
        with urllib.request.urlopen(request,data) as f:
            result = f.read().decode("utf-8")
        return result
