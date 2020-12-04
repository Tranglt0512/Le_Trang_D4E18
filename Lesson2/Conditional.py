#bilary,conditional and boolean 
# a=10
# b=20
# print("a>b:", a>b)
# print("a<b:",a<b)
# print("a=b:", a==b)
# if a>b:
#     print("a>b")
# if a<=b: 
#     print("a is smaller than b") 
#     print("b is greater than a")
# # if a>b:
# #     print("a is greater than b")
# # else:
# #     print("a is not greater than b")
# a = int(input("how old are you"))
# if a <=10:
#     print("free ticket, you are welcomed")
# elif 10<a<=20:
#     print("Half price, your ticket is 20$")
# else:
#     print("full price, 40$")
#BMI Health
weight = float(input("enter your weight"))
height = float(input("enter your height"))
BMI = weight/height**2
if BMI <18.5:
    print("underweight")
elif 18.5<=BMI<24.9:
    print("normal")
elif 24.9<=BMI<29.9:
    print("overweight")
else:
    print("obese")
#Quardratic equaltion ax**2+bx+c
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
delta=b**2-4*a*c
if delta>0:
    print("Phương trình có hai nghiệm")
    x1=(-b-math.sqrt(delta))/(2*a)
    print ("x1=:",x1)
    x2=(-b+math.sqrt(delta))/(2*a)
if delta<0:
    Prnit("Phương trình có 1 nghiệm")
    x=()
