#import urllib.request as req
#from bs4 import BeautifulSoup as bs


import requests
#get 요청
url = "http://www.naver.com"
responseGet = requests.get(url)
#print(responseGet.text) html텍스트 받는법
print(responseGet)


# 파라미터 전송방법 1
url = "http://www.naver.com?a=bbb&b=123"
responseGet = requests.get(url)
print(responseGet) # responseGet.status_code

# 파라미터 전송방법 2
paramDict = { "a" : "bbb", "b" : 123 }
url = "http://www.naver.com"
responseGet = requests.get(url, params=paramDict)
print(responseGet)


#Post 요청
url = "http://www.google.com"
responsePost = requests.post(url, data={'name':'python', 'description':'fileupload'},
                             files = {"file1":graphfile, 'file2':graphfile})
responsePost.status_code
responsePost.text # @RespnseBody가 있으면 값을 응답, uploadresult.jsp응답

