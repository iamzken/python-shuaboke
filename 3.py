#encoding=utf8
import urllib.request
import socket
socket.setdefaulttimeout(3)
of = open("proxy")
lines = of.readlines()
proxys = []
i_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTNmZGRlZjhhNmYxOGZkZTU3NmJkN2Y3ODNmYjkxYWU2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWxZMFhPaVRaMEpRaFhtdDQrZ3lmZEFWUXlYenJVcnBaT1B2ZjJ0MW5wK1E9BjsARg%3D%3D--f626e8500a3286dcf7550252b7c73289b4319f6b; CNZZDATA1256960793=140538128-1471419069-%7C1471419069',
    'Host':'www.xicidaili.com',
    'Pragma':'no-cache',
    'Referer':'http://www.xicidaili.com/nn/1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
}
for i in range(0,len(lines)):

    ip = lines[i].strip("\n").split(":")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener);
        req = urllib.request.Request(url,headers=i_headers)
        res = urllib.request.urlopen(req).read()
        print (res)
    except Exception as e:
        print (proxy)
        print (e)
        continue