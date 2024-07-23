'''n='101011'
k=len(n)-1
sum=0
for i in n:
    sum+=int(i)*2**k
    k=k-1
print(sum)'''

n=101011
sum=0
i=0
while n>0:
    rem=n%10
    pro=rem*pow(2,i)
    sum+=pro
    i+=1
    n=n//10
print(sum)
    
    