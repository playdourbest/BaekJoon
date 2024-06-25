# N개의 정수안에 X라는 정수가 있나?

import sys
r=range;#input=sys.stdin.readline
N=int(input());N_list=list(map(int,input().split()))
M=int(input());M_list=list(map(int,input().split()))
cnt={}
for i in N_list:
    cnt[i]=cnt[i]+1 if i in cnt else 1
for j in M_list:
    print(1 if j in cnt else 0)