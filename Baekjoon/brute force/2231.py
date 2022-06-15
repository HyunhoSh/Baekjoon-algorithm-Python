import sys

# n의 분해합 구하기

n = int(sys.stdin.readline())
num = 0

for i in range(7):
    if n//(10**i)==n:
        num = i-1
        break
# 12345
list_res = []
for i in range(n):
    res = 0
    str_i = str(i)
    list_i = list(str_i)
    for j in list_i:
        int_j = int(j)
        res+=int_j
    res+=i
    if res==n:
        list_res.append(i)

if len(list_res)==0:
    print(0)
else:
    list_res.sort(reverse=True)
    print(list_res[-1])


