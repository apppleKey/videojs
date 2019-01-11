

import requests
from bs4 import BeautifulSoup
from lxml import etree
url='https://www.douyu.com/cms/gong/201712/19/6921.shtml'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
def getImg():
    page=requests.get(url,headers=headers)
    # bs=BeautifulSoup(page.text)
    # for img in bs.find_all('img'):
    #         src=img['src']
    #         print(src)
    xpath=etree.HTML(page)
    video=xpath.xpath('//img')
    for img in video:
        print(img['src'])


if __name__ == "__main__":
    getImg()