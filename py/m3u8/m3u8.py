# -*- coding:utf-8 -*-  
import os
import sys
import requests
import datetime
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
def download(url):
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
        
    #新建日期文件夹
    download_path = os.path.join(download_path, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    #print download_path
    os.mkdir(download_path)
        
    all_content = requests.get(url).text  # 获取第一层M3U8文件内容
    if "#EXTM3U" not in all_content:
        raise BaseException("非M3U8的链接")
 
    if "EXT-X-STREAM-INF" in all_content:  # 第一层
        file_line = all_content.split("\n")
        for line in file_line:
            if '.m3u8' in line:
                url = url.rsplit("/", 1)[0] + "/" + line # 拼出第二层m3u8的URL
                all_content = requests.get(url).text
 
    file_line = all_content.split("\n")
 
    unknow = True
    key = ""
    for index, line in enumerate(file_line): # 第二层
        if "#EXT-X-KEY" in line:  # 找解密Key
            method_pos = line.find("METHOD")
            comma_pos = line.find(",")
            method = line[method_pos:comma_pos].split('=')[1]
            print ("Decode Method：", method)
            
            uri_pos = line.find("URI")
            quotation_mark_pos = line.rfind('"')
            key_path = line[uri_pos:quotation_mark_pos].split('"')[1]
            
            key_url = url.rsplit("/", 1)[0] + "/" + key_path # 拼出key解密密钥URL
            res = requests.get(key_url)
            key = res.content
            print ("key：" , key)
            
        if "EXTINF" in line: # 找ts地址并下载
            unknow = False
            pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1] # 拼出ts片段的URL
            #print pd_url
            
            res = requests.get(pd_url)
            c_fule_name = file_line[index + 1].rsplit("/", 1)[-1]
            
            if len(key): # AES 解密
                cryptor = AES.new(key, AES.MODE_CBC, key)  
                with open(os.path.join(download_path, c_fule_name + ".mp4"), 'ab') as f:
                    f.write(cryptor.decrypt(res.content))
            else:
                with open(os.path.join(download_path, c_fule_name), 'ab') as f:
                    f.write(res.content)
                    f.flush()
    if unknow:
        raise BaseException("未找到对应的下载链接")
    else:
        print ("下载完成")
    merge_file(download_path)
 
def merge_file(path):
    os.chdir(path)
    cmd = "copy /b * new.tmp"
    os.system(cmd)
    os.system('del /Q *.ts')
    os.system('del /Q *.mp4')
    os.rename("new.tmp", "new.mp4")
    
if __name__ == '__main__': 
    url = "https://pl-ali.youku.com/playlist/m3u8?vid=XNDAxNDIwODU2MA&type=flvhdv3&ups_client_netip=745d0cae&utid=0DGiFIKtYmYCAXo10TY%2BEq%2FS&ccode=0502&psid=371d8d6694ec0f4094f43c2bc358c4fb&duration=197&expire=18000&drm_type=1&drm_device=7&ups_ts=1547607552&onOff=0&encr=0&ups_key=96503923424d107b982a7e29da5168d1" 
    download(url)
