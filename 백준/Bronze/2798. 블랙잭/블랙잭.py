# N장의 카드를 숫자가 보이게 둠 - 3장의 카드를 고름
# 최대값 M 을 제시
from itertools import combinations as c
N,M=map(int,input().split());num=list(map(int,input().split()))
print(max(sum(x) for x in c(num,3) if sum(x) <= M))