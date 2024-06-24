# 1. 가지고있는 카드의 종류 및 갯수를 저장
# 2. 가지고있는 카드의 종류와 찾아야할 종류를 비교, 있다면 갯수 출력/없으면 0
import sys
r=range;input=sys.stdin.readline
N=int(input());N_list=list(map(int,input().split()))
M=int(input());M_list=list(map(int,input().split()))
cnt={}
for i in N_list:
    cnt[i] = cnt[i] + 1 if i in cnt else 1
for j in M_list:
    print(cnt[j] if j in cnt else 0, end=' ')