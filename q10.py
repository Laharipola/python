#removing duplicate words
'''n='hello world hello world good morning good afternoon'
n=n.split()
s=''
for i in n:
    if i not in s:
        s+=i+' '
print(s)'''

s='hello world hello world good morning good afternoon' 
s=s.split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s1=''
for k,v in d.items():
    if v>=1:
        s1+=k+' '
print(s1)
        
        