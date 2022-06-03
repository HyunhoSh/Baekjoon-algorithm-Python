import sys

n = int(sys.stdin.readline())

# 1 단계 1개, 2단계 (2*2-1)*2 + 0 + 0, 3단계 (3*2-1)*2 + 1 + 1, 4단계 (4*2-1)*2 + 2 + 2, 5단계 (5*2-1)*2 + 3 + 3
cnt = 1
sum = 1

if n==1:
    print(1)

else:
    while(1):
        cnt+=1

        res = (cnt*2-1)*2+2*(cnt-2)
        sum += res

        if n<=sum:
            break
    print(cnt)