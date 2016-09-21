import re
import urllib.request
from downloadimg import DownloadImg
from configparser import ConfigParser

'''
CONFIG = 'conf.txt'
config = ConfigParser()
config.read()
'''

url = 'http://g.e-hentai.org/g/978569/472c63c2e2/'
imgL = []
Headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }


req = urllib.request.Request(url,headers = Headers)
oper = urllib.request.urlopen(req)
findlink = re.compile('href="(http://g.e-hentai.org/s.+?)"')
data = oper.read().decode('utf-8')
for item in findlink.findall(data):
    if item:
        imgL.append(item)

page = 1

gate = DownloadImg(imgL,Headers)
all_pages = gate.Download(page)
print('All pages:',all_pages)








