'''arr=[1,1,0,1,1,0,0]
s1=''
s2=''
for i in arr:
    if i==0:
        s1+=str(i)+' '
    else:
        if i==1:
            s2+=str(i)+' '
            
print(s1+s2)'''

arr=[1,1,0,1,1,0,0]
ones=[]
zeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        if i==1:
            ones.append(i)
print(zeros+ones)