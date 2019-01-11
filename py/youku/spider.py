import urllib 
import requests
from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing.dummy import Pool  
# pool = Pool(4)  
# results = pool.map(crawl_func, urls_list)  
# pool.close()  
# pool.join()

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url='https://v.youku.com/v_show/id_XMzk2Mjk4ODM0MA==.html?spm=a2h0k.11417342.soresults.dposter&s=5b4c068434544699a22d'

def geturls():
    html=requests.get(url,headers=headers).text
    bsObj=BeautifulSoup(html)
    for item in bsObj.find_all('div',class_='item-cover'):
        href=item.a['href']
        print(href)
        # getVideopage(href)
        # break

# 打开视屏的播放页面
def getVideopage(url):
    html=requests.get('https:'+url,headers=headers).text
    xpath=etree.HTML(html)
    video=xpath.xpath('//*[@id="ykPlayer"]/div[1]/video[1]')
    print(video)
    return False
    # bsObj=BeautifulSoup(html)
    # playerDiv= bsObj.find("div",id_='module_basic_player')
    # print(playerDiv)

if __name__ == "__main__":
    geturls()