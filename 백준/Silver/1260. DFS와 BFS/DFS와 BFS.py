import sys

# DFS
def dfs(matrix, i, visited):
  visited[i] = True
  print(i, end=' ')
  for c in r(len(matrix[i])):
    if matrix[i][c] == 1 and not visited[c]:
      dfs(matrix, c, visited)

# BFS
from collections import deque
def bfs(matrix, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for c in range(len(matrix[value])):
        if matrix[value][c] == 1 and not visited[c]:
          queue.append(c)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    r=range;input=sys.stdin.readline
    n, m, v = map(int, input().split())
    matrix = [[0] * (n+1) for _ in r(n+1)]
    for _ in r(m):
      f, t = map(int, input().split())
      matrix[f][t] = matrix[t][f] = 1

    visited = [False] * (n+1)
    dfs(matrix,v,visited)
    print()
    visited = [False] * (n+1)
    bfs(matrix,v,visited)