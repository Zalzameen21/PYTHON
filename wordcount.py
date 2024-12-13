sen=input("enter the sentance")
word=input("enter the word")
sen=sen.split(" ")
count=0
for i in range(0,len(sen)):
    if word==sen[i]:
        count=count+1
print(count)        
