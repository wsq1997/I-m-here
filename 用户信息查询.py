# encoding:utf-8# encoding:utf-8
import urllib
import urllib2

'''
组内用户列表查询
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getusers"


params = {"end":100,"group_id":"test_group_2","start":0}
params = urllib.urlencode(params)

access_token = '24.368724ed4474f34a441020fb505fd349.2592000.1513003930.282335-10345332'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
