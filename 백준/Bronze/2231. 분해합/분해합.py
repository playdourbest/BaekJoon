# 분배합
# 245 의 분배합 = 245+2+4+5
# 256 의 생성자 = 254

import sys
r=range;input=sys.stdin.readline
# N=int(input());lst=[]
# for i in r(10):
#     for j in r(10):
#         for k in r(10):
#             A=100*i+10*j+k
#             B=N-(i+j+k)
#             if A==B:
#                 lst.append(A)
# if not lst:
#     print(0)
# else:
#     print(min(lst))

N=int(input())
output=0
for i in r(1,N+1):
    num=list(map(int,str(i)))
    output=sum(num)+i
    if output==N:
        print(i)
        break
    if i==N:
        print(0)