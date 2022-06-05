### Time over - Problem: Using Recursion
# import sys

# # sys.setrecursionlimit(10**7)

# d = [0]*10000000

# def factorisation(n,tmp):
#     cnt_local = 0
#     for u in range(1,n+1):
#         if n%u==0:
#             cnt_local+=1
#     if cnt_local==2:
#         print(n)
#     else:
#         if d[n]!=0:
#             return d[n]
#         if n%tmp==0:
#             n_ = n//tmp
#             print(tmp)
#             d[n] = factorisation(n_,tmp)
#             return d[n]
#         else:
#             d[n]= factorisation(n,tmp+1)
#             return d[n]
       
        

# n = int(sys.stdin.readline())

# if n ==1:
#     print(None)
# else:
#     # print(3)
#     factorisation(n,2)
#####################################################
### Refer to https://needneo.tistory.com/112
import sys

def factorisation(n):
    tmp = 2

    while tmp<=n:
        if n%tmp==0:
            print(tmp)
            n = int(n/tmp)

        else:
            tmp+=1

n = int(sys.stdin.readline())

factorisation(n)