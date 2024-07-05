import sys

def dfs(v):
    vis[v] = True
    for i in g[v]:
        if not vis[i]:
            dfs(i)
            
if __name__=='__main__':
    sys.setrecursionlimit(10000)
    r=range;input=sys.stdin.readline
    n,m = map(int,input().split())
    g = [[] for _ in r(n+1)]
    for _ in r(m):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    vis = [False for _ in r(n+1)]
    cnt = 0
    for i in r(1,n+1):
        if not vis[i]:
            cnt += 1
            dfs(i)
    print(cnt)