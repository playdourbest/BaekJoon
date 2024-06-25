# 1~N 이 원을 이루어 있음 -> deque 사용
# K번째를 제거 반복 -> roate 이용해서 선택
# 1,2,3,4을 예시로,
# 1을 기준으로 3번째라면 4지만, rotate 사용하면 1을 포함한 3번쨰라 값이 3이 나옴 -> 한칸씩 밀기
import sys
from collections import deque
r=range;input=sys.stdin.readline
N,K=map(int,input().split())
josephus=deque([i+1 for i in r(N)])
output=[]
for i in r(N):
    josephus.rotate(1-K)
    output.append(josephus[0])
    josephus.popleft()
print(str(output).replace('[','<').replace(']','>'))