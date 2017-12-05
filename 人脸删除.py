# encoding:utf-8
import urllib
import urllib2

'''
删除用户
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/delete"


params = {"uid":"test_user_5"}
params = urllib.urlencode(params)

access_token = '24.368724ed4474f34a441020fb505fd349.2592000.1513003930.282335-10345332'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
