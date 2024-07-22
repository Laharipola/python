s=input()
uc,lc,dc,sc=0,0,0,0
for c in s:
    if c.isupper():
        uc+=1
    elif c.islower():
        lc+=1
    elif c.isdigit():
        dc+=1
    else:
        sc+=1
if len(s)>8 and uc>0 and lc>0 and dc>0 and sc>0:
    print('valid')
else:
    print('Invalid')
