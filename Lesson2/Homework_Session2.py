#Bài 1
# x=int(input("insert year: "))
# if x%4==0:
#     print("366 days")
# else:
#     print("365 days")
#Bài 2:
# x=int(input("month: "))
# y=int(input("year: "))
# if x==2 and y%4==0:
#     print("29 days")
# elif x==2 and y%4!=0:
#     print("28 days")
# elif x==4 or x==6 or x==9 or x==11:
#     print ("30 days")
# else:
#     print("31 days")
#EX4:
# a=int(input("a:"))
# b=int(input("b: "))
# c=int(input("c: "))
# if a<b and b<c:
#     print(a,b,c)
# elif a<c and c<b:
#     print(a,c,b)
# elif b<a and a<c:
#     print(b,a,c)
# elif b<c and c<a:
#     print(b,c,a)
# elif c<a and a<b:
#     print(c,a,b)
# else:
#     print(c,b,a)
#EX3:
# x=int(input("month"))
# if 1<=x<=3:
#     print("spring")
# elif 4<=x<=6:
#     print("summer")
# elif 7<=x<=9:
#     print("fall")
# else:
#     print("winter")
#EX5:
# a=int(input("a:"))
# b=int(input("b: "))
# c=int(input("c: "))
# if (a+b)>c and (a+c)>b and3 (b+c)>a:
#     print("True")
#     if (a**2+b**2)==c**2 or (a**2 + c**2)==b**2 or (b**2+c**2)==a**2:
#         print("Tam giác vuông")
#     elif a==b or a==c or b==c:
#         print("Tam giác cân")
#     elif a==b==c:
#         print("Tam giác đều")
#     else:
#         print("Tam giác thường")
# else:
#     print("False")
#EX6:
x=float(input("số điện:"))
if x<=50:
    print("Số tiền mức 1",x*1.678)
    print("Tổng số tiền:",x*1.678)
elif 50<x<=100:
    M1=50*1.678
    print("số tiền mức 1",M1)
    M2=(x-50)*1.734
    print("số tiền mức 2",M2)
    print("tổng số tiền",M1+M2)
elif 100<x<=200:

    M1=50*1.678
    print("số tiền mức 1",M1)
    M2=100*1.734
    print("số tiền mức 2",M2)
    M3=(x-100)*2.014
    print("tổng số tiền",M1+M2+M3)
elif 200<x<=300:
    M1=50*1.678
    print("số tiền mức 1",M1)
    M2=100*1.734
    print("số tiền mức 2",M2)
    M3=200*2.014
    print("số tiền mức 3",M3)
    M4=(x-200)*2.536
    print("số tiền mức 4",M4)
    print("tổng số tiền",M1+M2+M3+M4)
elif 300<x<=400:
    M1=50*1.678
    print("số tiền mức 1",M1)
    M2=100*1.734
    print("số tiền mức 2",M2)
    M3=200*2.014
    print("số tiền mức 3",M3)
    M4=300*2.536
    print("số tiền mức 4",M4)
    M5=(400-x)*2.834
    print("số tiền mức 5",M5)
    print("tổng số tiền",M1+M2+M3+M4+M5)
elif x>400:
    M1=50*1.678
    print("số tiền mức 1",M1)
    M2=100*1.734
    print("số tiền mức 2",M2)
    M3=200*2.014
    print("số tiền mức 3",M3)
    M4=300*2.536
    print("số tiền mức 4",M4)
    M5=400*2.834
    print("số tiền mức 5",M5)
    M6=(x-400)*2.937
    print("số tiền mức 6",M6)
    print("tổng số tiền",M1+M2+M3+M4+M5+M6)