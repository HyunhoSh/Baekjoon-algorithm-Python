# Using Sieve of Eratosthenes
# Refer to https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
import sys

m,n = map(int, sys.stdin.readline().split())

def sieve_era(n):
    # n개의 요소에 True 설정(소수로 간주) (당연히 2부터)
    list_n = [True] * (n+1)
    
    # n의 최대 약수가 sqrt(n)이므로, sqrt(n)번째까지의 인덱스까지만 검사
    k = int(n**0.5) 
    
    for i in range(2,k+1):
        if list_n[i] == True:   # 소수라면
            for j in range(i+i,n+1,i): # i이후로 i의 배수들을 False 처리한다.
                list_n[j] = False
    # print(list_n)
    # 소수 리스트 리턴
    return [i for i in range(2,n+1) if list_n[i]==True and i>=m]

list_k = sieve_era(n) 

for j in list_k:
    print(j)    
