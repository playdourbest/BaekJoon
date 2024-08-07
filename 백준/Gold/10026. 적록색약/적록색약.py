# 현재 노드의 인접 노드를 탐색해야함.
# bsf로 탐색실시
# 탐색할때 적록색약인 경우 R과 G를 같은 색으로 취급
import sys
from collections import deque

r=range;input = sys.stdin.readline

def bfs(grid, visited, r, c, color, cb):
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        row, col = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
                if cb:
                    if (grid[new_row][new_col] in 'RG' and color in 'RG') or grid[new_row][new_col] == color:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))
                else:
                    if grid[new_row][new_col] == color:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

def count_areas(grid, cb):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in r(N):
        for j in r(N):
            if not visited[i][j]:
                cnt += 1
                bfs(grid, visited, i, j, grid[i][j], cb)
    return cnt

N = int(input())
grid = [input().strip() for _ in r(N)]
print(count_areas(grid, False), count_areas(grid, True))