

import requests
from bs4 import BeautifulSoup
from lxml import etree
from PIL import Image
from selenium import webdriver

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


def getImgs():
    driver = webdriver.PhantomJS()  #Run in Ubuntu, Windows need set executable_path.
    driver.maximize_window()
    driver.get('http://user.qzone.qq.com/{0}/photo'.format(self.qq))
    driver.implicitly_wait(20)
    imgs= driver.find_element_by_tag_name('img')
    for img in imgs:
        print(img)
    driver.close()
    driver.quit()



if __name__ == "__main__":
    getImgs()