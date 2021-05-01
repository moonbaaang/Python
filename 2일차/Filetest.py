# 파이썬 데이터 소스로부터 데이터를 가져와 분석 - 결과(파일 저장) 테이블, 그래프
# 파일 하나를 읽어 데이터를 가져옴
#open read write close

#파일 쓰기

import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.listdir()) # 위와 같은 의미
'''
# open('a.txt', 'r|w|a|b')
try:
    file = open("moduletest.py", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("파일명/경로를 확인하세요.")
file.close()
'''
''' # 파일이 없으면 새로 생성
file2 = open("a.txt" , "w")
file2.write("Create new text file")
file2.close()
'''

file2 = open("a.txt" , "a") # 파일없으면 새로 생성/ 파일 있으면 기존 내용 뒤 추가 쓰기 저장
file2.write("\nCreate new Line")
file2.close()

# 파일 한라인씩 읽어서 리스트에 저장
# file_list = []
file_list = list()
file3 = open("moduletest.py", "r", encoding="utf-8")
for line in file3:
    file_list.append(line)
file3.close()
'''
linenum = 1
for line in file_list:
    print(linenum,"번 라인", line)
    linenum = linenum+1
'''
# 위와 동일한 방법
for index in range(0, len(file_list), 1):
    print(index+1, "번 라인", file_list[index], end="")



# 라인번호가 있는 상태의 모든 내용을 파일 copy.txt에 저장
file4 = open("copy.txt", "w")

for index in range(0, len(file_list), 1):
    line = str(index+1)+"번 라인 :"+ file4[index]
    file4.write(line)
f4.close()

    
# useredcars.csv
# 마일리지 20000 이상이면 "폐차직전" 출력
# 마일리지 10000이상 ~ 20000미만  이면 "심각한 중고
# 10000미만 양호한 중고

# ex) 2011 , SEL , 21992, 7413, Yellow, AUTO "양호한 중고"










