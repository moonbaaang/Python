import urllib.request as req
from bs4 import BeautifulSoup as bs

response = req.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs(response, "html.parser")

city_list = soup.select("city")

'''
for city in city_list:
    wf = soup.select_one("wf")
    print(city.string+":"+wf.string)
'''

city_list = []
tmx_list = []
tmn_list = []

for loc in soup.select("location"):
    city_list.append(loc.select_one("city").string)
    tmx_list.append(loc.select_one("tmx").string)
    tmn_list.append(loc.select_one("tmn").string)

tmx_list = list(map(int, tmx_list))
tmn_list = list(map(int, tmn_list))

import matplotlib.font_manager as fm

'''
# 글꼴 리스트
fname_list = []
for f in fm.fontManager.ttflist:
    fname_list.append(f.name)
fname_list.sort()
for name in fname_list:
    print(name)
'''

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Batang"
plt.rcParams["font.size"] = 10
plt.rcParams["figure.figsize"] = (7, 7)
plt.rcParams["xtick.labelsize"] = 5 #데이터 글씨크기
plt.rcParams["axes.labelsize"] = 10 #레이블 글씨 크기
plt.rcParams["lines.linewidth"] = 2
plt.rcParams["lines.linestyle"] = '--'
plt.rcParams["axes.grid"] = True

plt.subplot(2, 1, 1)
plt.plot(city_list, tmn_list)
plt.subplot(2, 1, 2)
plt.plot(city_list, tmn_list)
plt.title("도시별 최고기온")
plt.xlabel("도시명")
plt.ylabel("max")
plt.show()
