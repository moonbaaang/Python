'''
usedcars.csv 파일 읽어
"폐차직전" "양호중고" "심각중고"

1> 폐차직전 몇개
양호중고 몇개
심각중고 몇개

2> 그래프 x축 레이블 - 상태, 데이터 - 폐차직전, 양호중고, 심각중고
y축 레이블 - 차량댓수 - 데이터 -----

'''

file = open("usedcars.csv", "rt")

total = 0
car_state = []
car_state_values = ["폐차직전", "심각한 중고", "양호한 중고"]
car_state_cnt = []
for line in file:
    total = total+1
    line_list = line.split(",")
    #year = line_list[0]
    #model = line_list[1]
    #price = line_list[2]
    mile = line_list[3]
    #color = line_list[4]
    #trans = line_list[5]

    if mile.isdigit() and int(mile) >= 20000:
        line_list.append(car_state_values[0])
    elif mile.isdigit() and int(mile)>=10000 and int(mile) <20000:
        line_list.append(car_state_values[1])
    elif mile.isdigit() and int(mile)<10000:
        line_list.append(car_state_values[2])
    else:
        line_list.append("차랑상태")
   # print(line_list)
    car_state.append(line_list[6]) # 한 대에 대한 차량 상태

for car_val in car_state_values: # 상태에 따른 차량 수
    car_state_cnt.append(car_state.count(car_val))


#print(car_state.count(car_val))

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Batang"
plt.rcParams["font.size"] = 10

plt.title("중고차 상태")
#plt.plot(car_state_values, car_state_cnt) 
# plt.hist(car_state_values, car_state_cnt) # x축, y축 빈도수
plt.hist(car_state[1:]) #x축 (150), y축 자동으로 빈도수 결정
plt.xlabel("차랑 상태")
plt.ylabel("차량 댓수")
plt.show()
