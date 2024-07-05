# 그림이 트리형태로 이루어짐 -> DFS,BFS 중 한개 사용
# 행렬로 표현하는건 올바르지 않기 때문에 그래프로 구현
import sys

def DFS(pair,visited):
    visited[pair]=True
    for j in graph[pair]:
        if not visited[j]:
            DFS(j,visited)
    return visited
        
if __name__=='__main__':
    r=range;input=sys.stdin.readline
    N=int(input())
    M=int(input())
    graph=[[] for _ in r(N+1)]
    visited=[False]*(N+1)
    for i in r(M):
        a,b=map(int,input().split())
        graph[a]+=[b]
        graph[b]+=[a]
    DFS(1,visited)
    print(sum(visited)-1)