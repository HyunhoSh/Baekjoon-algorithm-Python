# Referred to https://gudwns1243.tistory.com/63

# Using dictionary
import sys

n, m = map(int,sys.stdin.readline().split())

dic = {}

# {key: value} -> i: a
for i in range(1,n+1):
    a = sys.stdin.readline().rstrip() # removing '\n'
    dic[i] = a
    dic[a] = i

for j in range(m):
    input_ = sys.stdin.readline().rstrip()
    
    if input_.isdigit():
        print(dic[int(input_)])
    else:
        print(dic[input_])
