Headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }

url = 'http://g.e-hentai.org/g/977940/11d1abc3a6/'

import urllib.request
import urllib
import re

req = urllib.request.Request(url,headers=Headers)
oper = urllib.request.urlopen(req)
data = oper.read().decode('utf-8')
linkfind = re.compile('src="(.+?)"')
n = 1
for x in linkfind.findall(data):
    if 'http' in x and '.jpg' in x:
        print(x)
        req2 = urllib.request.Request(x,headers=Headers)
        with open('D://Test//%d.jpg' % n , 'wb') as f:
            f.write(urllib.request.urlopen(req2).read())

    
    
    
