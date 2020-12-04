import math
# age=input('How old are you?')
# print("I am", 2020 - int(age))
#BMI
height=input("what is your height")
print("I am", height)
weight=input("what is your weight")
print('I am', weight)
print('Your BMI is',round((float(weight)/float(height)**2), 2))

#Area/perimeter of circle
#round(number,number_of_digit)
radius=input("enter the radius")
print("the perimeter is", round(float(radius)*2*math.pi,2))
print("the area is", float(radius)*float(radius)*3.14)