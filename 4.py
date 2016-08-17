#coding:utf-8
import urllib.request

def url_user_agent(url):
    #设置使用代理
    proxy = {'http':'http://123.57.190.51:7777'}
    proxy_support = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler(debuglevel=1))
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    #添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
    # i_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib.request.Request(url,headers=i_headers)
    html = urllib.request.urlopen(req)
    if url == html.geturl():
        doc = html.read()
        return doc
    return

url = 'http://www.dianping.com/search/category/2/10/g311'
doc = url_user_agent(url)
print (doc)