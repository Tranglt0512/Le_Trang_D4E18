a= range(10)
print(*a)
#Range(stop): *range: from 0 to the value before stop
print(*range(5))
#*range(start,stop): range from the start to before the stop
print(*range(5,10))
#range(start_value, stop_value,step): range from the start to before the start, stepping "step"
#print(*range(20,0,-1)) #20 - 1
print(*range(20,0,-1)) 
print(*range(20,0,-3))
