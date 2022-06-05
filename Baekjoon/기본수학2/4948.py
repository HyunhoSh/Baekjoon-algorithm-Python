import sys

def sieve(n):
    m = 2*n
    sieve = [True]*(m+1)

    k = int(m**0.5) # 루트값 지정

    for i in range(2,k+1):
        if sieve[i]==True:
            for j in range(i+i,m+1,i):
                sieve[j]=False
        
    return [k for k in range(2,m+1) if sieve[k]==True and k>n and k<=m]

list_int = []

while(1):
    n = int(sys.stdin.readline())
    if n==0:
        break
    else:
        list_int.append(n)

for i in list_int:
    list_tmp = sieve(i)
    # print(list_tmp)
    print(len(list_tmp))