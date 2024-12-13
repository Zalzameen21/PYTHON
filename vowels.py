vowels="AEIOUaeiou"
a=input("Enter the word")
b=[]
for i in a:
    if i in vowels:
        b.append(i)
print(b)
        
