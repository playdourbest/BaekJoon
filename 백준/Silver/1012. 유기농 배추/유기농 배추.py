import sys
sys.setrecursionlimit(10000)
r=range;input=sys.stdin.readline
dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def DFS(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if field[x][y]==1:
        field[x][y]=0
        for i in r(4):
            DFS(x+dx[i],y+dy[i])
        return True
    return False

output=[]
for _ in r(int(input())):
    M,N,K=list(map(int,input().split()))
    field=[[0]*M for _ in r(N)]
    for _ in r(K):
        x,y=map(int,input().split())
        field[y][x]=1
    cnt=0
    for i in r(N):
        for j in r(M):
            if DFS(i,j):
                cnt+=1
    print(cnt)