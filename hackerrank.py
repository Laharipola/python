s=7
t=11
a=3
b=15
apples=[6,5,-4]
oranges=[9,8,-4]
acount=0
bcount=0
for i in range (len(apples)):
    if 7<= apples[i]+a <= 11:
        acount+=1
for i in range (len(oranges)):
    if 7<= apples[i]+b <= 11:
        bcount+=1
print(acount,bcount)