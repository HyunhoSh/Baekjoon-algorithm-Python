### Referred to https://yoonsang-it.tistory.com/12
import sys

t = int(sys.stdin.readline())

fin = []

for i in range(t):
    list_tmp = []
    k = int(sys.stdin.readline()) # 층
    n = int(sys.stdin.readline()) # 호
    ppl = [u for u in range(1,n+1)] # 1~n까지 저장

    for j in range(k):
        for m in range(1,n):
            print(ppl) # 실시간 확인용
            ppl[m] += ppl[m-1]
            
    print(ppl[-1])
# 3층 4호일 때
# [1, 2, 3, 4]  # 0층 1~4호 (각 인덱스)
# [1, 3, 3, 4]  
# [1, 3, 6, 4]
# [1, 3, 6, 10] # 1층 1~4호
# [1, 4, 6, 10]
# [1, 4, 10, 10]
# [1, 4, 10, 20] # 2층 1~4호
# [1, 5, 10, 20] 
# [1, 5, 15, 20]
# 마지막은 [1,5,15,35] -> 3층 1~4호이고, 마지막 원소가 3층 4호

# ppl[-1]은 누적 거주민 수
