# 인접한것끼리 한개로 묶고 특징 찾기 -> 탐색
# 행렬형태로 주어줬음 -> 인접행렬 DFS 또는 BFS로 구현가능
# 인접행렬 DFS 재귀함수로 구현

# <input>
# 첫째줄, N = 지도의 크기
# 다음줄 = N개의 정보값
# <output>
# 첫째줄, 총 단지수
# 다음줄, 오름차순으로 각 단지 내 집의 수

import sys
sys.setrecursionlimit(10000)
r=range;input=sys.stdin.readline

def DFS(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return 0
    if field[x][y]==1:
        field[x][y]=0
        cnt=1
        for i in r(4):
            cnt+=DFS(x+dx[i],y+dy[i])
        return cnt
    return 0

if __name__ == '__main__':
    N=int(input())
    field=[list(map(int,input().strip())) for _ in r(N)]
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]

    apt_lst=[]
    for i in r(N):
        for j in r(N):
            if field[i][j]==1:
                apt=DFS(i,j)
                if apt>0:
                    apt_lst.append(apt)
    
    apt_lst.sort() # 오름차순
    print(len(apt_lst)) # 총 단지수
    for i in apt_lst:
        print(i) # 단지내 집의 수