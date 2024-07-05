# 계단오르기
# 1. 한번에 오를수 있는 최대 계단은 1개 or 2개
# 2. 연속해서 3개 밟으면 X. ex) 3,4,5번째 오르기 불가
# 3. 마지막 계단은 무조건 밟아야함
# 계단의 개수가 300개 이하 -> 배열을 301개 만들기

import sys
r=range;input=sys.stdin.readline
N=int(input())
stair=[0]*301 # 총 계단값 초기화
for i in r(1,N+1):
    stair[i]=int(input())

# 계단 오르는 경우의수 계산 알고리즘
# 1,2,4 vs 1,3,4 중에 더 큰값
# 1,2,4,5 vs (1,3,5 vs 2,3,5)
data=[0]*301
data[1]=stair[1]
data[2]=stair[1]+stair[2]
data[3]=max(stair[1]+stair[3],stair[2]+stair[3])

for j in r(4,N+1):
    data[j]=max(data[j-3]+stair[j-1]+stair[j],data[j-2]+stair[j])
print(data[N])