#변수 연산자 조건문 반복문 문법
#자바 int i = 10
#자바스크립트 let j = 20

'''
k = None # null과 같은
print(type(k))
k = 30
print(type(k))
k = 3.14
print(type(k))
k=True #파이썬에서는 boolean type 첫번째 대문자
print(type(k))
k='abc'
print(type(k))

# 파이썬 1개값 저장 변수타입 - int float bool str NoneType
# 연산자
a=10
b=3 
print("a/b=", a/b) #실수몫
print("a//b=", a//b) #정수몫
print("a%b=", a%b) #나머지
print("a를 2진수로 =", bin(a)) #2진수
print("a를 16진수로 =", hex(a)) #16진수
print("a를 8진수로 =", oct(a)) #8진수
print("3.14-3.04 = ", 3.14-3.04)

# 문자 관련 연산자
a="abcdefg"
b="def"
c=100
print(a+b) #+c는 불가능
print(a*3)
'''
d='''모듈 basic.py 파이썬 소스파일-모듈 파이썬 설치포함 다른모
듈 찾는방법 구글링 '''
'''
print(d)

print(a[2:4])
print(a[2:])
print(a[-1:4]) # 나오지않

a='multicampus'
print('cam' in a)
# cam 위치가 몇번 인덱스인지
print(a.find('cam'))
print(a.rfind('cam'))
#a 변수에서 cam문자열부터 나머지 문자열 출력
print(a[a.find('cam'):])

print(a.count('m')) # m 문자 갯수
print(len(a)) # 총 문자 갯수
# print(dir(a)) # str 타입 포함 함수 목록 확인

a='multi'
b='python'
c=100 #str 타입변경
print("{0}는 정수이고 {1}는 문자열입니다".format(c,a))


#10//3 , math.trunc(10/3), round(10/3)
print("{:+10.2f}".format(10/3))
print("{:10d}".format(10//3))


# 정수 -> 문자열
print(type(str(100)))
print(type(100))

print("abc"+"def"+str(100))

# 문자열 -> 정수
# 파이썬
in1 = input("정수 한개를 입력해주세요")
print(int(in1))

fo1 = input("실수 한개를 입력해주세요")
print(float(fo1))
print(in1+fo1)

bol=input("논리값 한개를 입력해주세요")
print(bool(bol))
# True true false False 0 모두 가
'''
'''
test1 = "abcdefg"
print("문자열테스트", test1[-1])

import sys
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
# ['C:/kdigital/python_source/basic.py', 'python', '100', 'pro']
# Run ... Customized 로 입력값 입력
'''


'''
주석
print(d)
import math
a=math.log10(100)
print(a)
a=3
b=2
print("math.pow(a,b) = ", math.pow(a,b))
print("math.trunc(a,b) = ", math.trunc(a/b))
# print("math.abc(-10) =", math.abs(-10)) abs함수는 기본 내장함수

#파이썬 기본 내장함수
print("abs(-10) = ", abs(-10))
print("round(a/b) = ", round(a/b))


#파이썬 기본 내장함수 확인
#print(dir(__builtins__))
'''


# 파이썬은 여러개 타입의 데이터 저장 가능 - 리스트 튜플 셋 딕셔너리
# 리스트 = 자바 동적배열 / 파이썬 여러 타입 데이터를 저장
# : [0] + * in

# List
a = ["title", 30, 400.5, True, [9,8,7]]
a2 = [1,2,3,4,5]
print(type(a))

print(a[0])
print(a[1:3])
print(a+a2)
print(a2*5) # 내용에 5를 곱하는것이 아님
print(1 in a2)

a.append(100) # 마지막에 추가
print("len(a) = ", len(a))
print(a[5])
a.insert(1, 200) # 설정한 인덱스에 추가
print("a.insert(1,200) after len(a) = ", len(a))
a[1] = 300 # 해당 인덱스 값 변경
print(a[1])
print("List a = ", a)
print(len(a[5]))

a.pop() # 리스트 마지막 데이터를 삭제
print(a)
a.remove(30) # 해당 데이터 값 삭제
print(a)
#a.remove(1000) # 존재하지 않는 데이터 삭제
#print(a)

del a[0] # 0번 인덱스 데이터 삭제
print(a)

a2.append(0)
print(a2)
a2.sort()
print(a2)
a2.reverse()
print(a2)

# Tuple : 값을 변경할 수 없는 리스트 (조회만 가능, 인덱스, 슬라이스는 가능)
d= (1,2,3,4,5)
print(type(d))
print(d[0])
#del d[0]
#d[0] = 100
#d.append[100]
c = 1,2,3,4,5 #()없는 튜플
print(c, type(c))
a,b = 1,2 #각각 변수에 튜플데이터 저장
print(a, type(a))
print(b, type(b))


# Dictionary : 자바 map(key, value) 쌍데이터 모음, 인덱스가 없다.
c={'name':'lee', "2":200, 'id':'lee'}
print(type(c))
print(c.items())
print(c.keys())
print(c.values())
print('id' in c)
c['id']='python' #id에 대한 값을 수정 (key is already used)
c['email']='A' # email 값 추가 (key is not defined)

print(c)

d={'seq':1, 'title':'제목', 'content':"내용",
   'addfiles':["a.png", "b.doc", "c.ppt"]}
print(d)
#print(d.items())
print(d.get("addfiles"))
print(d['addfiles'][0])
d.pop('content')
print(d)

# Set - 인덱스 없고, value만 있다. 중복 데이터를 가질 수 없다.
b = {1,2,3,4,5}
print(type(b))
print(len(b))
b.add(5) # append func do not use
print(b)

print("#####################################################")
# 6장 조건문
if 10>5:
    print(1)
else:
    print(2)
'''
a = input("정수를 입력하세요 (0입력시 시스템 중단) : ")
a = int(a)
if a == 0:
    print("0으로 나누기 불가능")
else:
    print("3을 {}로 나눈 결과는 {}입니다 = ".format(a, 3/a))

print("프로그램 종료")
'''

# switch-case > match-case 조건문 추가
'''
import sys
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

kor = int(sys.argv[1])
mat = int(sys.argv[2])
eng = int(sys.argv[3])

total = kor+mat+eng
avg = total/3

if avg>= 90:
    grade = 'A'
elif avg>=80:
    grade = 'B'
elif avg>=70:
    grade = 'C'
elif avg>=60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
'''
import random

num = 99
num = random.randint(1,100)
if num%2 ==1:
    print(num,"은 홀수입니다")
else:
    print(num, "은 짝수입니다")
'''
num = input("정수 입력하세요")
num = num[len(num)-1]
if num in "02468":
    print("짝수")
elif num in "13579":
    print("홀수")
else:
    print("정수 타입이 아닙니다")
'''
print("#############################")
'''
while 조건식 :
    반복 수행 문장
for 변수 in 반복할 수 횟수:
    반복 수행 문장;

count = 1
total = 0
while count <= 10:
    print(count)
    total = total+count
    count = count + 1;
print(total)

mynum = 50
count = 0;
while True:
    inputnum = int(input("숫자를 맞춰보세요"))
    if mynum > inputnum:
        print("입력값보다 큽니다. 다시 시도해보세요")
        count = count +1
    elif mynum < inputnum:
        print("입력값보다 작습니다. 다시 시도해보세요")
        count = count +1
    else:
        print("정답입니다 대단하시네요")
        break
    if count==10:
        print("실패하셨습니다")
        break

import random
lottoset = set()
while True:
    lottonum = random.randint(1,45)
    lottoset.add(lottonum)
# random.randrange(1,46) (46은 포함하지 않음)
    if len(lottoset)==6:
        break
       
print(sorted(lottoset))
'''
'''
import random
lottoset = set()
cnt=0
while True:
    lotto = random.randrange(1,46)
    cnt = cnt+1
    print("{} 번째 난수 {} 를 생성합니다".format(cnt, lotto))
    lottoset.add(lotto)
    if len(lottoset)==6:
        break
       
print(sorted(lottoset))
'''

for i in range(11):
    print(i)
    
a = [1,2,3,4,5]

for i in a:
    num = i*i
    print(num)

d = {'key':1, 'key2':2, 'key3':3, 'key4':'string'}
for i in d.items():
    print(i)
#키, 값이 () 형태로 한 쌍으로 나온다.
for key, value in d.items():
    print('{}의 값은 {}입니다.'.format(key, value))        

for i in range(0, len(a), 1):
    print("{}번째 인덱스 값은 {}입니다.".format(i, a[i]))


print("##############################################")

'''
def 함수명(매개변수):
    문장:
    문장:
    return 값;

리턴결과변수 = 함수명(매개변수);

주의할 점 : 내장 함수 변수와 같은 이름으로 만들지 말것
'''

# 매개변수가 없는 함수
def hello_3times():
    for i in range(1,4):
        print('hello');
# 실행
hello_3times();
print(hello_3times());
# 아래 print문은 return 값이 없으므로 None 반환


# 매개변수가 있는 함수
def message_3times(message):
    for i in range(1,4):
        print(message);
message_3times("안녕") # 자바스크립트에서는 매개변수가 남는 것은 오류처리 X

# 매개변수 두개
def message_ntimes(message, n):
#    type(n)=='int' 타입 확인
    for i in range(1, n+1, 1):
        print(message);
message_ntimes('python study', 5)

# 기본 매개변수가 있는 함수 정의
def basic_ntimes(message='java study', n=5):
#    type(n)=='int' 타입 확인
    for i in range(1, n+1, 1):
        print(message);
basic_ntimes('spring', n=10)

print(10, 20, sep=":", end="!!")
print(10, 20, sep=":", end="!!")

# 가변 매개변수 (*msg, n) 이러한 식으로 선언할 시 불가능
# 가변 매개변수는 1개만 선언가능, 일반매개변수와 같이 선언 시 항상 일반매개변수 뒤에
#선언되어야한다.
# (n, *msg)로 선언 시엔 가능하다.
def dynamic_message(n, *msg):
    for i in msg:
        print(i)

dynamic_message('\npython', 'testteststestset')
dynamic_message('python', 'java');
dynamic_message('python', 'java','spring');

