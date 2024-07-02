# 피보나치 수열 그대로 구현하면 됨
import sys
r=range;input=sys.stdin.readline
for _ in r(int(input())):
    N=int(input())
    a,b=1,0
    for _ in r(N):
        a,b=b,a+b
    print(a,b)