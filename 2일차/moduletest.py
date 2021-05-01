# module
# 물리적 - *.py
# 미리 만들어진 py파일을 사용
# pypi.org 라이브러리 다운로드

# import 방법 
import math
from math import trunc, log
from math import *
import math as ma

a1 = math.trunc(3.14)
print(a1)

import random
print(random.randint(1, 100))
print(random.randrange(1,101))
name_list = ["a", "b", "c", "d", "e", "가나라바나"]
print(random.choice(name_list))
random.shuffle(name_list)
print(name_list)
print(random.sample(name_list, 2))


import sys
print(sys.version)
print(sys.getwindowsversion())
print(sys.path) #내장 모듈 + 사용자 모듈 + 외부설치 추가 모듈


import os
print(os.name)
print(os.getcwd())
print(os.listdir())
# os.rename('파일명' , '') 자바에서 File Class 가 하는 역할
# os.remove('파일명' , '')

import datetime

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

after_oneyear = now.replace(year=(now.year+1))
print("1년 뒤", after_oneyear.year)

import time
sec = time.time() #초단위로 시간을 나타냄
print(sec)
loc = time.localtime() #년월일시분초 
print(loc.tm_year)

# 아직 설치되지 않은 모듈 설치 - import - 사용코드
# 도스 pip3 > python install p(ackage)(?)

# 파일 데이터 분석 , 기상청 정보, 특정지역 xxx정보 그래프,
# 외부파일, 외부서버 접속, 데이터 분석 최적화

# 웹서버 데이터 전송 - spring server와 연결 가능
# 웹서버의 데이터를 가져오는 방법 - 웹 크롤링
'''
beautifulsoup 패키지= *.py 들= 패키지
python 설치 pip.exe 명령어 같이 설치
외부에서 필요한 파이썬 라이브러리 설치 가능하게 한 명령어
pip3 install beautifulsoup패키지명
pypi.org - beautifulsoup4 4.9.3 검색 후 설치 명령어 복사, dos창에 붙여넣기
pip list 로 설치 확인
pip show beautifulsoup4 로 경로 등 정보확인
'''
import sys
print(sys.path)

# beautifulsoup4 사용 

import urllib.request as req
from bs4 import BeautifulSoup as bs

response = req.urlopen("http://127.0.0.1:9090/semi/")
soup = bs(response, "html.parser")

#전체 내용 출력
#rescontents = soup.prettify()
#print(rescontents)

# 특정 태그만 출력 (ex <h3>태그 )
print(soup.find("h1"))  # type - dictionary , string:xxx, style:xxx
print(soup.find("h1").string)
#print(soup.find("img")['src']) # 이미지 파일의 경로를 속성처럼 가져올 수 있
print(soup.findAll('h3')) # h3 태그를 모두 가져옴
# find - select_one() / findAll - select()

for h3 in soup.findAll('h3'): #h3 태그의 string 값을 모두 가져옴
    print(h3.string)


response.close()
#print(response)
