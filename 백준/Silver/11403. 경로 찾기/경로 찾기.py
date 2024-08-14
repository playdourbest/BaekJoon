# 플로이드 워셜 알고리즘으로 구현하면 됨.

import sys
r=range;input=sys.stdin.readline

def bakjoon_11403(graph, N):
    reach = [[0] * N for _ in r(N)]
    for i in r(N):
        for j in r(N):
            reach[i][j] = graph[i][j]
    for k in r(N):
        for i in r(N):
            for j in r(N):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1
    
    return reach

N = int(input())
graph = [list(map(int, input().split())) for _ in r(N)]
result = bakjoon_11403(graph, N)

for i in result:
    print(' '.join(map(str, i)))