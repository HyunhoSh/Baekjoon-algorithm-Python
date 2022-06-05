# Refer to https://yoonsang-it.tistory.com/31

### My code -> Time over
# import sys

# fin = []

# def sieve(n):
#     sieve = [True]*(n+1)
#     global fin
#     k = int(n**0.5)

#     for i in range(2,k+1):
#         if sieve[i] == True:
#             for j in range(i+i,n+1,i):
#                 sieve[j]=False
#     fin = [k for k in range(2,n+1) if sieve[k]==True]
    
#     idx = 0
#     # tmp = fin[idx]
#     # print(tmp)
#     list_tup = []
#     while(idx<len(fin)):
#         tmp = fin[idx]

#         for i in range(len(fin)):
#             r = n-tmp
#             if r==fin[i]:
#                 if r>=tmp:
#                     # print(1)
#                     # print(str(tmp)+' '+str(r))
#                     list_tmp = []
#                     list_tmp.append(tmp)
#                     list_tmp.append(r)
#                     list_tup.append(list_tmp)
#                     break
#                 # else:
#                 #     print(3)
#                 #     print(str(r)+' '+str(tmp))
#                 #     list_tmp = []
#                 #     list_tmp.append((tmp,r))
#                 #     list_tup.append(list_tmp)
#                 #     break
#         idx+=1
#     # print(list_tup)
#     for j in list_tup[-1]:
#         print(j,end=' ')


# t = int(sys.stdin.readline())

# list_n = []

# for i in range(t):
#     list_n.append(int(sys.stdin.readline()))
# # print(list_n)
# for j in list_n:
#     sieve(j)
#     print('')

##############################
## Answer - Refer to https://yoonsang-it.tistory.com/31

def Sieve():
    check = [True] * 10001
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(100001):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Sieve()