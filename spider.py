# -*- coding =utf-8 -*-
# @time : 2021/5/2 20:53
# @Author : Rov
# @File : spider.py
# @Software : PyCharm
# import requests
# url='https://www.bilibili.com/read/cv3849974'
# params={
#     'type':'recommend',
#     'page_num':0,
#     'page_size':45
# }
# headers={
#     'User-Agent':'Mozilla/5.0(WindowsNT6.1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/58.0.3029.110Safari/537.36',
#     'Accept-Encoding':'gzip,deflate'
# }
# html=requests.get(url=url , params=params, headers = headers).text
import requests
from bs4 import BeautifulSoup as BSoup
import os
import wget

if not os.path.exists('pic'):
    os.mkdir('pic')

path = r'C:\Users\Rov\Desktop\电力系统暂态过程（常鲜戎&赵书强主编）课后部分习题解答+暂态分析常见计算习题和解答 - 哔哩哔哩专栏.html'
htmlfile = open(path, 'r', encoding='utf-8')
tmlhandle = htmlfile.read()
soup = BSoup(tmlhandle, 'lxml')
figure_ls = soup.body.find_all('figure')
pic_url = []
for i in figure_ls:
    try:
        i.img.attrs['data-src']
        pic_url.append('http:' + i.img.attrs['data-src'])
        #data-src内的url缺少http:
    except:
        continue
print("总共有%d个图片",len(pic_url))
i=0
s='a'
try:
    while(1):
        wget.download(pic_url[i], out=r"./pic/%s.png"%(s+str(i)[-1]))
        if str(i)[-1]=='9':
            s = chr(ord(s) + 1)
            print("超出上限,开始进行%s"%s)
        i=i+1
except:
    print("完成")
# for i in pic_url:
#     os.system('wget -P pic "' + i + '"')
#     #这里我指定在pic文件内
#     #wget -P path 指定存放路径