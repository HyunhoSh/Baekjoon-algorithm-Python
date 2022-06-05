import sys

n = int(sys.stdin.readline())

fin = 0

list_n = list(map(int, sys.stdin.readline().split()))
# print(list_n)
for j in list_n:
    cnt = 0
    for k in range(1,j+1):
        if j%k==0:
            cnt+=1
    if cnt==2:
        fin+=1
print(fin)
