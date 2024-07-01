# 중요도가 높은것이 있다면 지금 인쇄해야할것을 맨 뒤로 보낸다
# ex) 2 1 4 3 이라면 4,3,2,1, 순으로 인쇄한다
# deque사용하면서 idx 생성해서 구별해야할듯?

import sys
from collections import deque
r=range;e=enumerate;input=sys.stdin.readline
for _ in r(int(input())):
    N,M=map(int, input().split())
    Q=deque([(i,idx) for idx,i in e(deque(map(int, input().split())))])
    cnt=0
    while True:
        # Q에 저장된 값에서 i 를 기준으로 최대값 찾아 비교
        if Q[0][0]==max(Q,key=lambda x:x[0])[0]:
            cnt+=1
            if Q[0][1]==M:
                print(cnt)
                break
            else:Q.popleft()
        else:Q.append(Q.popleft())