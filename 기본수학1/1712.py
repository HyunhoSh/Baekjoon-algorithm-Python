import sys

# a -> 고정 비용, b -> 가변 비용, c -> 노트북 가격
a,b,c = map(int,sys.stdin.readline().split())

if c>b:
    print(int(a/(c-b)+1))

elif c<b or c==b:
    print(-1)