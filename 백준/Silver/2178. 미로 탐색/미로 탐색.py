import sys
from collections import deque

def bfs(x, y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in r(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[n-1][m-1]
    
if __name__=='__main__':
    sys.setrecursionlimit(10000)
    r=range;input=sys.stdin.readline
    n,m=map(int,input().split())
    graph=[]
    
    for _ in r(n):
        graph.append(list(map(int,input().rstrip())))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(bfs(0,0))