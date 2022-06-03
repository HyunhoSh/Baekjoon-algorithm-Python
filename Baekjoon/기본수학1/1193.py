import sys

x = int(sys.stdin.readline())

tmp = 0
sum = 0

while True:
    tmp = tmp+1
    sum = sum + tmp

    if (x<=sum):
        break

# print(x)
# print(tmp)
# print(sum)

if x == 1:
    print('1/1')

else:
    
    if tmp%2==1:
        a = 1 + (sum-x)
        b = tmp - (sum-x)
    else:
        # print(tmp)
        # print(sum)
        a = tmp - (sum-x)
        b = 1 + (sum-x)
    
    print(str(a)+'/'+str(b))

    