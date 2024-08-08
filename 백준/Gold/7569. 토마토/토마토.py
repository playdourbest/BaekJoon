from collections import deque
import sys
r=range;input=sys.stdin.readline

def baekjoon_7569_bfs(tomato, N, M, H):
    direct = [
        (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
    ]
    q = deque()
    day = -1
    for h in r(H):
        for m in r(M):
            for n in r(N):
                if tomato[h][m][n] == 1:
                    q.append((m, n, h))
    while q:
        day += 1
        for _ in r(len(q)):
            m, n, h = q.popleft()
            for dm, dn, dh in direct:
                new_m, new_n, new_h = m + dm, n + dn, h + dh
                if 0 <= new_n < N and 0 <= new_m < M and 0 <= new_h < H:
                    if tomato[new_h][new_m][new_n] == 0: # 익지 않은 토마토
                        tomato[new_h][new_m][new_n] = 1 # 익게 만든다
                        q.append((new_m, new_n, new_h))
    # 모든 토마토가 익었는지 확인
    for h in r(H):
        for m in r(M):
            for n in r(N):
                if tomato[h][m][n] == 0: # 익지 않은 토마토가 남아있다면
                    return -1
    return day
N, M, H = map(int, input().split())
tomato = []
for _ in r(H):
    box = []
    for _ in r(M):
        row = list(map(int, input().split()))
        box.append(row)
    tomato.append(box)

print(baekjoon_7569_bfs(tomato, N, M, H))