# double pointer

arr=[1,5,2,3,4]
k=6
count=0
f=0
l=len(arr)-1
while f<1:
    if arr[f]+arr[l]==k:
        count+=1
    elif arr[f]+arr[l]<k:
        f+=1
    else:
        l-=1
f+=1
l-=1
print(count)