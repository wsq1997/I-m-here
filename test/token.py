# -*- coding: cp936 -*-
import urllib, urllib2, sys
import ssl

# client_id Ϊ������ȡ��AK�� client_secret Ϊ������ȡ��SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6utnDxWqueQEKI0T6ZkgwBjv&client_secret=VVUM82N68ax7iphKIPEWicdcc1wW1bIP'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
