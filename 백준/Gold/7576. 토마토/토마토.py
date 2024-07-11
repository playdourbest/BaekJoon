# 익은 토마토가 있으면 인접한 안익은 토마토에 영향을 미침
# M(x좌표) 와 N(y좌표) 가 주어짐
# 인접한 정보부터 탐색 -> BFS

# <input>
# M(x좌표),N(y좌표) = 상자의 크기 (2<= M,N <=1000)
# N개의 줄에 토마토 위치 표현
# M개의 토마토 상대 표현(-1:없음, 0:안익음, 1:익음) 
# <output>
# 모두 익을때 최소날짜 , 모든 토마토가 익어있는 상태면 1 , 모두 안익으면 -1

import sys
from collections import deque
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in r(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                queue.append((nx,ny))

if __name__=='__main__':
    r=range;input=sys.stdin.readline
    M,N=map(int,input().split())
    box=[list(map(int,input().split())) for _ in r(N)]
    queue=deque()
    for i in r(N):
        for j in r(M):
            if box[i][j]==1:
                queue.append((i,j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    bfs()
    
    day=0
    state=True
    for i in r(N):
        for j in r(M):
            if box[i][j]==0:
                state=False
            day=max(day,box[i][j])
    if state:
        print(day-1)
    else:
        print(-1)