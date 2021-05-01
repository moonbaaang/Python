# 함수, 모듈 , 예외처리


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

def dynamic_message2(n, *msg):
    n=3
    for i in range(1, n+1, 1):
        print(msg)

dynamic_message2(5, 'spring', 'python', True)



def dynamic_message3(*msg, n): # 가변 매개변수를 앞에 설정 시
    for i in msg:
        print(i)

dynamic_message3('하나', '둘', n=5) # 반드시 일반 매개변수를 정확하게 설정해주어야함
# 또는 def dynamic_message3(*msg, n=10) 으로 기본값을 설정해도 됨(키워드매개변수)

# 함수 - 입력값(매개변수) - 기능 구현문장 - 리턴값

# 리턴값이 정수를 갖는 함수 정의
def return1_func():
    print("리턴 전")
    return 0

r1 = return1_func()
print(r1)

# 리턴값이 없는 함수 정의
def return2_func():
    print("리턴 전")
    return

r1 = return2_func()
print(r1) #None

# 리턴값이 여러개 함수 정의 : 자동 tuple 함수 정의
def return3_func():
    return 1,2,3,4,5; # 튜플로 합쳐 리턴

r1 = return3_func()
print(r1)
print(r1[0])
print(type(r1))

# 값을 튜플이 아닌 리스트로 전달하고싶다면?
def return4_func():
    return [1,2,3,4,5] # 리스트로 전달만 하면 됨 / set {}

r1=return4_func()
print(r1)
print(r1[0])
r1[0]=10
print(r1[0])

def return5_func():
    return {1:1, 2:2, 3:3}

r1 = return5_func()
print(r1)


# 매개변수 지역변수 전역변수
a = "전역변수 a"
def vartest(b):
    a = "지역변수 a"
    c = "지역변수"
    print(a)
    print(b)
    print(c)

def vartest2(d):
    e = "다른 지역변수"
    print(a)
    print(d)
    print(e)

vartest("매개변수1")
vartest2("매개변수2")
# 지역변수는 함수가 실행될 동안만 메모리 내 할당

a = "전역변수 a"
def vartest3(b):
    global a
    a = "전역변수 값 수정" # 전역변수를 가져와 사용
    c = "지역변수"
    print(a)
    print(b)
    print(c)

vartest3("매개변수3")
print(a)


global_var = 0
def inc():
    local_var = 1
    local_var = local_var + 1
    # global_var = global_var + 1 실행 불가능 (global 키워드 선언해야함)
    global global_var
    global_var = global_var + 1
    print("지역변수값 {}, 전역변수 값 {}입니다.".format(local_var,global_var))

inc()
inc()
inc()
inc()
inc()

# 반복문 팩토리얼 구현
def fact1(n):
    result = 1
    for i in range(1, n+1, 1):
        result = result * i
        print("{}!은 {}입니다".format(i, result))
    return result

print(fact1(5))

# 재귀호출 팩토리얼 함수2, 단, 성능은 떨어짐 
def fact2(n):
    if n==0:
        return 1
    else:
        result = n*fact2(n-1)
        print("{}!은 {}입니다".format(n, result))
        return result


print(fact2(5))

# 자바스크립트와 파이썬은 함수를 변수 취급 가능
# 함수를 매개변수, 지역함수, 리턴함수로 활용

# 함수를 매개변수로 활용 (Callback함수)
def f1():
    print("출력")
'''
import time

def call_func(f):
    # f1이 함수이면 5초 뒤 실행
    # 자바스크립트에서는 setTimeout(함수 , 5000)
    # 자바에서는 Thread.sleep(변수, 5000)
    time.sleep(5)
    f() # 전달매개변수가 함수이면 ()를 붙임


call_func(f1)
'''

# map 함수(함수를 매개변수로)
a= [2.5, 4.7, 3.6, 3.4]
print(a)
a = list(map(int, a))
print(a)

b = ["java programming과정", "oracle sql", "spring framework", "python programming"]
# 첫문자만 대문자, 대문자 변경
def my_upper(s):
    return s[:4].upper() + s[4:]

print(my_upper(b[0]))

b = map(my_upper, b) #매개변수는 b 리스트가 가지고있다는 의미

for i in b:
    print(i)

def no_action():
    pass

no_action()

# 람다식 - 리턴문 하나만 가지는 무명의 함수 / 정의와 동시에 호출

def lamb():
    return 0;
print(lamb()) # 이 과정을 람다식으로 표현

# (lambda 매개변수 : 리턴값)(매개변수 값)
print((lambda : 0)())
print((lambda x : x*x)(10))
print((lambda x, y : (x+y, x-y, x*y, x/y))(10, 2))
