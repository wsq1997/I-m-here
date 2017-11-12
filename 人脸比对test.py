# encoding:utf-8
import base64
import urllib
import urllib2

'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

f = open('E:\u=349831126,1438562339&fm=58.jpg', 'rb')
# 参数images：图像base64编码
img1 = base64.b64encode(f.read())
# 二进制方式打开图文件
f = open('E:\u=3909680289,342355042&fm=27&gp=0.jpg', 'rb')
# 参数images：图像base64编码
img2 = base64.b64encode(f.read())

params = {"images":img1 + ',' + img2}
params = urllib.urlencode(params)

access_token = '24.368724ed4474f34a441020fb505fd349.2592000.1513003930.282335-10345332'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
