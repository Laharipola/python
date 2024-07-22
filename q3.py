s='a1b2c3d492nm45'
m=''
n=''
for i in s:
    if i.isdigit():
        m+=i
    else:
        n+=i
print(m+n)
