s=int(input("entr a starting number:"))
e=int(input("enter a ending number:"))
ps=[]
for i in range(s,e+1):
    if i ** 0.5==int(i**0.5):
        num=str(i)
        if all(int(digit)%2==0 for digit in num):
            ps.append(i)
print(ps)
