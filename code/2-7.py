# coding:utf-8

# __author__ = 'zhangkenan'
# __date__   = '2016/8/17'
# __Desc__   = '测试测试  刷新自己的博客的浏览量'

import urllib.request,re,socket
from bs4 import BeautifulSoup

def getHtml(url,headers):
    req = urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

def parse(data):
    content = BeautifulSoup(data,'lxml')
    return content

def getReadNums(data,st):
    reg = re.compile(st)
    return re.findall(reg,data)

url = 'http://blog.csdn.net/zkn_cs_dn_2013/article/details/52639972'
headers = {
    'referer':'http://blog.csdn.net/zkn_cs_dn_2013',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}
socket.setdefaulttimeout(10)
proxy = {'http':'http://121.40.108.76:80'}
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
i = 0
while i<100000000:
    try:
        html = getHtml(url,headers)
        content = parse(html)
        result = content.find_all('span',class_='link_view')
        #print (result[0].get_text())
        print ("success")
        i = i + 1
    except Exception as e:
        print ("error")
        continue;