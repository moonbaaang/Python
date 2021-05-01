# useredcars.csv
# 마일리지 20000 이상이면 "폐차직전" 출력
# 마일리지 10000이상 ~ 20000미만  이면 "심각한 중고
# 10000미만 양호한 중고

# ex) 2011 , SEL , 21992, 7413, Yellow, AUTO "양호한 중고"



file = open("usedcars.csv", 'r')
car_list = []
for line in file:
    line.replace("\n","")
    car_list.append(line.split(","))

del car_list[0]
file.close()


file1 = open("usedcars.txt", 'w')
for index in car_list:
    if int(index[3]) >= 20000:
        index.append("폐차 직전")
        file1.write(str(index))
        file1.write("\n")
    elif int(index[3]) < 20000 and int(index[3])>=10000:
        index.append("심각한 중고")
        file1.write(str(index))
        file1.write("\n")
    else:
        index.append("양호한 중고")
        file1.write(str(index))
        file1.write("\n")
    

file1.close()


file1 = open("usedcars.txt", "r")
cnt = 1
for i in file1:
    print(cnt,"번째 항목 :", i, end="")
    cnt = cnt+1
file1.close()
