# refer to www.youtube.com/watch?v=FYCGV6F1NuY

import sys

n = int(sys.stdin.readline())

# hanoi(원반개수, 시작, 목표, 보조) -> 여기선 시작이 1, 목표가 3, 보조가 2
# 원리 -> 제일 큰 원판을 제외한 나머지 원판을 모두 보조 기둥으로 옮기고 그 다음 단계
# -> 보조기둥을 일단 목표 기둥으로 설정해놓고 시작 -> hanoi(원반개수-1, 시작, 보조(2번, 목표 역할), 목표(3번, 보조 역할))
# 그 다음은, 보조 기둥인 2번이 시작점, 목표 기둥은 원래의 목표 기둥, 1번의 시작점 기둥은 보조 기둥 역할을 함 
# -> hanoi(n-1, 보조(2번이 시작 역할), 목표(3번), 시작(1번이 보조 역할))

def hanoi(n, start,end,assistance):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,assistance,end)
    print(start,end)
    hanoi(n-1,assistance,end,start)

print(2**n-1)
hanoi(n,1,3,2)
