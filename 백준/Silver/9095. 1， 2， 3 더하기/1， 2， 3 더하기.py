# 정수 N이 주어질 때, 1,2,3 을 이용해 나타내는 수를 구하기
# T = 첫째 줄 테스트 케이스 수
# N = 정수
# 테이블에 값 저장해서 경우의 수 모두 찾기로 구현

import sys

def cnt_num(N):
    lst=[0]*(N+1)
    lst[0]=1
    for i in r(1,N+1):
        if i>=1:
            lst[i]+=lst[i-1]
        if i>=2:
            lst[i]+=lst[i-2]
        if i>=3:
            lst[i]+=lst[i-3]
    return lst[N]

if __name__=='__main__':
    r=range;input=sys.stdin.readline
    
    for _ in r(int(input())):
        N=int(input())
        print(cnt_num(N))