import sys
r=range;input=sys.stdin.readline

def bakjoon_14500_dfs(x, y, depth, total):
    global max_sum
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            bakjoon_14500_dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def find():
    global max_sum
    for i in r(N):
        for j in r(M):
            visited[i][j] = True
            bakjoon_14500_dfs(i, j, 1, board[i][j])
            visited[i][j] = False
            if i >= 1 and j >= 1 and j < M - 1:  # ㅗ형태
                total = board[i][j] + board[i-1][j] + board[i][j-1] + board[i][j+1]
                max_sum = max(max_sum, total)
            if i < N - 1 and j >= 1 and j < M - 1:  # ㅜ형태
                total = board[i][j] + board[i+1][j] + board[i][j-1] + board[i][j+1]
                max_sum = max(max_sum, total)
            if i >= 1 and i < N - 1 and j < M - 1:  # ㅏ형태
                total = board[i][j] + board[i-1][j] + board[i+1][j] + board[i][j+1]
                max_sum = max(max_sum, total)
            if i >= 1 and i < N - 1 and j >= 1:  # ㅓ형태
                total = board[i][j] + board[i-1][j] + board[i+1][j] + board[i][j-1]
                max_sum = max(max_sum, total)

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in r(N)]
    visited = [[False] * M for _ in r(N)]
    max_sum = 0
    find()
    print(max_sum)