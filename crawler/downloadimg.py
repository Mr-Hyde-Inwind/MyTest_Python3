import re
import urllib.request
from configparser import ConfigParser

CONFIG = 'conf.txt'
config = ConfigParser()
config.read(CONFIG)

PATH = config.get('PATH','DownloadPath')

class DownloadImg(object):
    def __init__(self,urls = [],headers = {}):
        self.Urls = urls
        self.headers = headers
    def Download(self,page):
        for url in self.Urls:
            req = urllib.request.Request(url,headers = self.headers)
            oper = urllib.request.urlopen(req)
            data = oper.read().decode('utf-8')
            linkfind = re.compile('src="(.+?)"')
            for item in linkfind.findall(data):
                if 'http' in item and '.jpg' in item:
                    req2 = urllib.request.Request(item,headers = self.headers)
                    try:
                        with open(PATH + '%d.jpg' % page,'wb') as gate:
                            gate.write(urllib.request.urlopen(req2).read())
                        page = page+1
                    except:continue
        return page


if __name__ == '__main__':
    url = ['http://g.e-hentai.org/s/d568c96ee9/977940-1']
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
    test = DownloadImg(url,headers)
    Tpage = test.Download(1)
    print(Tpage)
