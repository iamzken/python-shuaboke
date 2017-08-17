#proxy_handle = urllib.request.ProxyHandler({'http':random.choice(proxy_list)})
#opener = urllib.request.build_opener(proxy_handle)
#response = opener.open(url)

#encoding=utf8
import urllib.request
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib.request.Request(url,headers=header)
res = urllib.request.urlopen(req).read()

soup = BeautifulSoup(res,'lxml')
ips = soup.findAll('tr')
f = open("proxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[1].contents[0]+":"+tds[2].contents[0]+"\n"
    print (tds[1].contents[0]+":"+tds[2].contents[0])
    f.write(ip_temp)

# def getHtml(url,headers):
#     req = urllib.request.Request(url,headers=headers)
#     page = urllib.request.urlopen(req)
#     html = page.read()
#     return html

# def parse(data):
#     content = BeautifulSoup(data,'lxml')
#     return content

# def getReadNums(data,st):
#     reg = re.compile(st)
#     return re.findall(reg,data)

# url = 'http://www.xicidaili.com/nn/1'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
# }
# i = 0
# while i<100:
#     html = getHtml(url,headers)
#     content = parse(html)
#     result = content.find_all('span',class_='link_view')
#     print (result[0].get_text())
#     i = i +1