file = open('usedcars.csv', 'r')

total = 0
for line in file:
    line_list = line.split(",")
    year = line_list[0]
    model = line_list[1]
    price = line_list[2]
    mile = line_list[3]
    color = line_list[4]
    trans = line_list[5]

    if mile.isdigit() and int(mile) >= 20000:
        line_list.append("폐차직전")
    elif mile.isdigit() and int(mile)>=10000 and int(mile) <20000:
        line_list.append("심각한 중고")
    elif mile.isdigit() and int(mile)<10000:
        line_list.append("양호한 중고")
    else:
        line_list.append("차랑상태")
    print(line_list)
    total = total+1

print("차량 총 댓수", total) 
    
file.close()

# 데이터 전처리가 필요
# 예) 마일리지값이 존재하지 않으면 이후 처리
