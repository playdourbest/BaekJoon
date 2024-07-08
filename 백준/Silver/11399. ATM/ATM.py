# N명의 사람
# i번 사람이 돈을 인출하는데 걸리는 시간 -> pi
# 예시를 확인하면, 시간이 적게 걸리는 순서대로 나열하면 가장 작은값이 나옴
import sys
r=range;input=sys.stdin.readline

N=int(input());time=list(map(int,input().split()))
time.sort()
output,time_sum=0,0
for i in r(N):
    time_sum+=time[i]
    output+=time_sum
print(output)