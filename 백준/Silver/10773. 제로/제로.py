# 0 입력되었을 때, 바로 앞 숫자 삭제
# 값을 입력할때마다 리스트에 append
# 0 이 입력된다면 append 를 실행하지 않고 pop 해버리면?
# 0 과 바로 앞의 숫자를 삭제하는 효과가 생김

import sys
r=range;input=sys.stdin.readline
lst=[]
for i in r(int(input())):
    if num:=int(input()):
        lst.append(num)
    elif lst:
        lst.pop()
print(sum(lst))

# for i in r(int(input())):lst.pop() if (num:=int(input()))==0 else lst.append(num)