#smallest prime number
def isprime(num):
    if num in(0,1):
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
            return True
n=int(input())
nextNum = n+1
while True:
     if isPrime(nextNum):
        print(nextNum)
        break
    nextNum += 1
    
        