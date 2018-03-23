import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'http://www.weather.com.cn/weather/101280601.shtml'  # 数据地址,从浏览器copy
# url = 'http://www.weather.com.cn/weather15d/101280601.shtml'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML'
                  ', like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
}

req = requests.get(url, headers=header)
req.encoding = 'utf-8'  # 防止中文乱码

soup = BeautifulSoup(req.text, 'html.parser')
# 分析得出 <ul class="t clearfix"> 标签下记录了我们想要的数据,因此只需要解析这个标签
ul_tag = soup.find('ul', 't clearfix')  # 利用css查找

# 每一天数据
li_tag = ul_tag.findAll('li')
for tag in li_tag:
    shijian = tag.find('h1').string
    tianqi = tag.find('p', 'wea').string
    fengli = tag.find('p', 'win').find('i').string
    # try:
    # gaowen = tag.find('p', 'tem').find('span').string
    # diwen = tag.find('p', 'tem').find('i').string
    a = {'时间': [shijian], '天气': [tianqi], '风力': [fengli]}
    b = DataFrame(a)
    # print(b)
    b.to_excel('商品信息.xlsx')
    # except:
    #     print('没有高温或低温数据')
    #     pass
    # # print(tag.find('p', 'win').find('i').string)  # 风力

    # print("_______________ 分割线 ____________________")
