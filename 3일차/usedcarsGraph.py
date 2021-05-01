file = open('usedcars.csv', 'rt')

total = 0
car_state = []
car_state_values = ["폐차직전", "심각한 중고", "양호한 중고"]
car_state_cnt = []
for line in file:
    total = total+1
    line_list = line.split(",")
    mile = line_list[3]

    if mile.isdigit():
        if int(mile) >=20000:
            line_list.append(car_state_values[0])
        elif int(mile) >= 10000 and int(mile) < 20000:
            line_list.append(car_state_values[1])
        elif int(mile) < 10000:
            line_list.append(car_state_values[2])
    else:
        line_list.append("차량상태")

    car_state.append(line_list[6])

for car_val in car_state_values:
    car_state_cnt.append(car_state.count(car_val))

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Batang'
plt.rcParams['font.size'] = 10

plt.title("중고차상태")
plt.hist(car_state[1:])
plt.xlabel("차량 상태")
plt.ylabel("차량 댓수")
plt.savefig("usedcarsGraph.jpg")
plt.show()
