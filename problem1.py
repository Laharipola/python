#n=int(input())
#k=int(input())
#arr = list(map(int,input().split(" ")))
#for i in range(n-k):
   # print(arr[1:4
n=5
k=3
arr=[2,4,6,8,9]
ans=32
for i in range(0,n-k+1):
    sub_arr=arr[i:i+k]
    print(sub_arr)
    sum=0
    for ind in range(1,k+1):
        sum+=sub_arr[ind-1]*ind
    print(sum)
    if sum>ans:
        ans=sum
