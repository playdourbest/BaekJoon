# N=4 일때
# 1. 가장 윗장 버리기 [2,3,4]
# 2. 남아있는 카드의 가장 윗장을 맨 아래로 보내기 [3,4,2]
# 3. 가장 윗장 버리기[4,2]
# 4. 남아있는 카드의 가장 윗장을 맨 아래로 보내기 [2,4]
# 5. 가장 윗장 버리기 [4]
import sys
r=range;input=sys.stdin.readline
# N=int(input());cards=[i+1 for i in r(N)]
# while len(cards)>=2:
#     cards.append(cards[1])
#     del cards[:2]
# print(cards[0]) # 시간초과

from collections import deque
n = int(input());cards = deque(r(1,n+1))
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])