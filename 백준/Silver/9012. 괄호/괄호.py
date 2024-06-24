# () -> YES
# ()) -> NO
# (( -> NO
# 괄호를 열면 닫아야함.
import sys
r=range;input=sys.stdin.readline
for _ in r(int(input())):
    T_list = list(input().strip())
    balance = 0
    valid = True
    for char in T_list:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                valid = False
                break
    if balance != 0:
        valid = False
    print('YES' if valid else 'NO')