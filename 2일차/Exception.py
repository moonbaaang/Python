for i in range(1, 11, 1):
    print(i)
# 자바 c c++ c# - 컴파일 언어 = 문법 검사 > 바이너리코드로 변경 (컴파일 과정) > 실
# 자바스크립트, 파이썬 - 인터프리터 언어 = 한문장마다 문법 검사, 실행

# 파이썬은 변수에 값이 설정되어야 메모리에 할당
'''
try:
    print(a)
except:
    print("a변수가 선언되지 않았습니다")

try:
    print(a)
except NameError:
    print("a변수가 선언되지 않았습니다")

try:
    print(a)
except ValueError:
    print("a변수가 선언되지 않았습니다")
'''

try:
    money = input("대출금액, 상환개월수 입력 : ") # 10000, 12입력
    two_items = money.split()
    loan = int(two_items[0])
    payback = int(two_items[1])
    if payback <= 0: #의도적 오류 발생
        raise ValueError("상환 개월수는 0 또는 음수값을 입력할 수 없습니다.")
    monthly_return = loan/payback
except IndexError:
    print("값을 입력하셔야합니다.")
except ValueError as ve:
    print(ve) #"대출금액이나 개월수는 정수만 입력가능합니다."
else: # 오류없이 정상 실행되었을 때  
    print(monthly_return , "을 매달 상환하셔야 합니다")
finally:
    print("영업 종료")

