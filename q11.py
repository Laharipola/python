#find next alphabet
'''s='abcdz'
for i in s:
    print(chr(ord(i)+1))'''
    
s='abcdz'
s1=''
for i in s:
    if ord(i)>=97 and ord(i)<122:
        s1+=chr(ord(i)+1)
    else:
        s1+=chr(ord(i))
print(s1)
