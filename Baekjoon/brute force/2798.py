import sys

n,m = map(int,sys.stdin.readline().split())

list_n = list(map(int,sys.stdin.readline().split()))
list_n.sort(reverse=True) # 내림차순

# tmp = list_n[0]

sum_list = sum(list_n)

if sum_list<=m:
    res = 0
    res = list_n[0] + list_n[1] + list_n[2]

else: # sum_list>m
    list_res = []
    for i in range(n):
        for j in range(i):
            for k in range(j):
                res = list_n[i]+list_n[j]+list_n[k]
                list_res.append(res)
    
    list_res.sort(reverse=True)

    for i in list_res:
        if i<=m:
            print(i)
            break
            

        
    