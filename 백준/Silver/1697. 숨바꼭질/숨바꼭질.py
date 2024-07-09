# 수빈 : 현재 점 N에 위치
# 동생 : K에 위치
# 이동 -> 1초후 X-1 또는 X+1
# 순간이동 -> 1초후 2*X
# 최단거리 찾기 -> BFS으로 구현하기

# <BFS 구현할 때 들어가야하는 내용>
# 1. 배열 초기화
# 2. 같은위치인 경우 return 값
# 3. 현 위치와 이동 카운트
# 4. 이동 가능한 값(X-1, X+1, 2*X)과 이동 후 이동한 카운트를 +=1
# 5. 한번 이동한 곳은 표시하기

from collections import deque as q
import sys

def baekjoon_1697_BFS(N, K):
    if N==K:
        return 0
    visited=[False]*100001
    queue=q([(N,0)])
    while queue:
        current_position,current_time = queue.popleft()
        visited[current_position]=True
        next_positions=[current_position-1,current_position+1,2*current_position]

        for next_position in next_positions:
            if 0<=next_position<=100000 and not visited[next_position]:
                if next_position==K:
                    return current_time+1
                queue.append((next_position,current_time+1))
                visited[next_position]=True
    return -1

if __name__=='__main__':
    input=sys.stdin.readline
    N,K=map(int,input().split())
    print(baekjoon_1697_BFS(N,K))
