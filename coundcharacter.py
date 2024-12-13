rst=str(input("enter a string"))
fr={}
for ch in st:
    
    if ch in fr:
        fr[ch]+=1
    else:
        fr[ch]=1
print(fr)
