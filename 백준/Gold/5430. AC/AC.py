from collections import deque
import sys

r=range;input=sys.stdin.readline

T = int(input().strip())
output = []

for _ in r(T):
    p = input().strip()
    n = int(input().strip())
    if n == 0:
        array = deque()
        input().strip()
    else:
        array = deque(map(int, input().strip()[1:-1].split(',')))
    rev = False;error = False
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if array:
                if rev:
                    array.pop()
                else:
                    array.popleft()
            else:
                output.append("error")
                error = True
                break
    if not error:
        if rev:
            array.reverse()
        output.append("[" + ",".join(map(str, array)) + "]")

print(*output, sep='\n')