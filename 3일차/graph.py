import matplotlib.pyplot as plt
import random

a = [1,2,3,4,5]
b = [2,4,6,8,10]

plt.plot(a,b)
plt.title("a, b")
plt.xlabel("a")
plt.ylabel("b")
#plt.savefig("test.png")
#plt.show()


c = []
for i in range(1, 11 ,1):
    c.append(random.randint(1, 10))

#plt.hist(c)
#plt.show()

plt.subplot(2, 1, 1) # 행 열 번호
plt.plot(a,b)

plt.subplot(2, 1, 2)
plt.hist(c)

plt.show()

