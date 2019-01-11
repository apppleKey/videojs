# -*- coding:utf-8 -*-
from lxml import etree

import urllib
import os
import requests

urllib2=urllib.request
def getHtml(url):
    html = requests.get(url).content
    selector = etree.HTML(html)
    return selector


def getContent(htm, xpathStr):
    selector = htm
    content = selector.xpath(xpathStr)
    return content

def getFlv(cons, title, folder):
    fn = '%s' % title
    pa = os.path.dirname(__file__) + '/' + 'youku/' +  folder
    # check and create folder
    if not os.path.exists(pa):
        os.mkdir(pa)
    fl = pa + '/%s.flv' % fn
    r = requests.get(cons)
    with open(fl, "wb") as code:
        code.write(r.content)

# = = = = = = #
videourl = 'http://vali-dns.cp31.ott.cibntv.net/677291A877B4371B0BE6B26B1/03000A0E0459E2A50507CC06C0F0FCD8579A8C-BBC1-7677-178F-9B250EB2777D.mp4?ccode=0502&duration=391&expire=18000&psid=a1c4a14d5cea8e5c246067056079be79&ups_client_netip=7a35d136&ups_ts=1546925450&ups_userid=&utid=0DGiFIKtYmYCAXo10TY%2BEq%2FS&vid=XMzA4NjI3ODUxMg&vkey=A473cfcc2618c0a28365fcb325b90e207&sp=180'
format = 'high'  # 'high'  'normal'  'super'

url = 'http://www.flvcd.com/parse.php?kw=' + urllib.parse.quote(videourl) + '&format=' + format
print(url)
req = urllib2.Request(url)
req.add_header('Referer', 'http://www.flvcd.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
res = urllib2.urlopen(req)

html = res.read()
# print html
selector = etree.HTML(html)

# get flv title
xp_title='//*[@id="subtitle"]'
htm0=getHtml(videourl)
cons=getContent(htm0,xp_title)
title=cons[0].text
print(title)

# get flv href
xp = '//*[@class="mn STYLE4"]//@href'
content = selector.xpath(xp)
print (content)

x=0
for con in content:
    if 'http://k.youku.com' in con:
        print (con)
        getFlv(con,  '%s' % x, title)
        # urllib.urlretrieve(con, getPath('%s' % x, title))# , callbackfunc)
        x+=1