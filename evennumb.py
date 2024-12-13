main=[1,2,3,4,5,6,7,8,9,10]
main_even=[]
main_odd=[]
for num in main:
    if num % 2 == 0:    
       main_even.append(num)
    else:
       main_odd.append(num)
print("main is equal to :",main)       
print("main_even :",main_even)
print("main_odd :",main_odd)
             
