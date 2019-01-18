import requests
import urllib
import os
import sys

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

def get_url_list(host, body):
	lines = body.split('\n')
	ts_url_list = []
	for line in lines:
		if not line.startswith('#') and line != '':
			if line.startswith('http'):
				ts_url_list.append(line)
			else:
				ts_url_list.append('%s/%s' % (host, line))
	return ts_url_list

def get_host(url):
	urlgroup = urlparse(url)
	return urlgroup.scheme + '://' + urlgroup.hostname

def get_m3u8_body(url):
	print( 'read m3u8 file:', url)
	session = requests.Session()
	adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=10)
	session.mount('http://', adapter)
	session.mount('https://', adapter)
	r = session.get(url, timeout=10)
	return r.content

def download_ts_file(ts_url_list, download_dir):
	i = 0
	for ts_url in reversed(ts_url_list):
		i += 1
		file_name = ts_url[ts_url.rfind('/'):]
		curr_path = '%s%s' % (download_dir, file_name)
		print ('\n[process]: %s/%s' % (i, len(ts_url_list)))
		print ('[download]:', ts_url)
		print ('[target]:', curr_path)
		if os.path.isfile(curr_path):
			print ('[warn]: file already exist')
			continue
		urllib.urlretrieve(ts_url, curr_path)

def main(url, download_dir):
	host = get_host(url)
	body = get_m3u8_body(url)
	ts_url_list = get_url_list(host, body)
	print ('total file count:', len(ts_url_list))
	download_ts_file(ts_url_list, download_dir)

if __name__ == '__main__':
	# args = sys.argv
	# if len(args) > 2:
	# 	main(args[1], args[2])
	# else:
	# 	print ('Fail, params error, try:')
	# 	print ('python', args[0], 'your_m3u8_url', 'your_local_dir\n')
    path=r"D:\Users\vender\Desktop\videojs\py\m3u8\download"
    url="https://pl-ali.youku.com/playlist/m3u8?vid=XNDAxNDIwODU2MA&type=flvhdv3&ups_client_netip=745d0cae&utid=0DGiFIKtYmYCAXo10TY%2BEq%2FS&ccode=0502&psid=371d8d6694ec0f4094f43c2bc358c4fb&duration=197&expire=18000&drm_type=1&drm_device=7&ups_ts=1547607552&onOff=0&encr=0&ups_key=96503923424d107b982a7e29da5168d1"
    main(url,path)