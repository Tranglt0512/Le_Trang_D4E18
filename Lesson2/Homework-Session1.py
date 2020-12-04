import math
#Bài 1
#a
# x1=float(input("insert x1"))
# print("y1=:",4*(x1**2+10*x1*math.sqrt(x1)+3*x1+1))
#b
# x2=float(input("insert x2"))
# print("y2=:",(math.sin(math.pi*x2**2+math.sqrt(x2**2+1))/(math.e**(2*x2)+math.cos((math.pi/4)*x2))))

#Bài 2
# X=int(input("nhập số tiền"))
# print("số tờ 100000:",(x//100000))
# print("số tờ 50000:",(x%100000)//50000)
# print("số tờ 20000:",(x%100000)%50000//20000)
# print("số tờ 10000:",(x%100000)%50000%20000//10000)
# print("tổng số tờ:",(x//100000)+(x%100000)//50000+(x%100000)%50000//20000+(x%100000)%50000%20000//10000)
#Bài 3
x=int(input("nhập số có ba chữ số:"))
print("Tổng của các chữ số là",((x//100)+(x%100)//10+(x%100)%10/1))


