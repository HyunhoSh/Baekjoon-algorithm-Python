import sys

# n -> 처음 n 개의 문자열이 집합 S
# m -> 그 다음 m 개의 문자열들
n,m = map(int, sys.stdin.readline().split())

list_n = []

for i in range(n):
    list_n.append(str(sys.stdin.readline()))

set_n = set(list_n)

list_m = []

for j in range(m):
    list_m.append(str(sys.stdin.readline()))

cnt = 0

for k in list_m:
    if k in set_n:
        cnt+=1

print(cnt)