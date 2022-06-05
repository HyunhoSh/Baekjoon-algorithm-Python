import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

fin = 0

prime_number = []

for i in range(m,n+1):
    cnt = 0 
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        prime_number.append(i)

if len(prime_number)==0:
    print(-1)
else:
    sum = 0

    for k in prime_number:
        sum+=k
    
    print(sum)
    # print(prime_number)
    print(prime_number[0])
        