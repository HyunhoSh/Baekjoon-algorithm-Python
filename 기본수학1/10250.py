import sys

t = int(sys.stdin.readline())

list_n = []

for i in range(t):
    list_k = list(map(int, sys.stdin.readline().split())) # H, W , N -> 층 수, 각 층의 방 수, 몇 번째 손님
    list_n.append(list_k)

for j in list_n:
    h = j[0]
    w = j[1]
    n = j[2]

    # quotient, remainder
    q = n/h  # 호 수
    r = n%h   # 층 수

    if(n%h==0):  # 층은 꼭대기, 호수는 몫
        q = n//h # 몫이 아닌 나누기 연산자를 사용하면 실수형으로 값이 저장되기 때문에 몫을 구하는 연산자 사용
        if q>=10:
            str_q = str(q)
        else:
            str_q = '0'+str(q)
        print(str(h)+str_q)
    else:
        q = (n//h)+1 # 호 수
        if q>=10:
            str_q = str(q)
        else:
            str_q = '0'+str(q)
        r = n%h
        str_r = str(r)
        print(str_r+str_q)

   
