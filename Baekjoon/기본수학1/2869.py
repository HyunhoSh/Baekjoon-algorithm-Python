import sys
import math

a,b,v = map(int, sys.stdin.readline().split())

## 시간 초과
# sum = 0
# cnt = 0

# while(1):
#     cnt+=1
#     sum +=a
#     if sum>=v:
#         break
#     sum -=b

## 답안
cnt = (v-b)/(a-b)

print(math.ceil(cnt))