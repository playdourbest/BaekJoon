import sys
r=range;input=sys.stdin.readline

M=int(input())
S=set()
output=[]

# 메모리 초과(리스트에 append 후 출력해서 그런듯?)
# for _ in r(M):
#     lst = input().split()
#     c = lst[0]

#     if c == 'add':
#         S.add(int(lst[1]))
#     elif c == 'remove':
#         S.discard(int(lst[1]))
#     elif c == 'check':
#         output.append(1 if int(lst[1]) in S else 0)
#     elif c == 'toggle':
#         x = int(lst[1])
#         if x in S:
#             S.remove(x)
#         else:
#             S.add(x)
#     elif c == 'all':
#         S = {i for i in range(1, 21)}
#     elif c == 'empty':
#         S.clear()
# print(*output, sep='\n')

for _ in r(M):
    lst = input().split()
    c = lst[0]

    if c == 'add':
        S.add(int(lst[1]))
    elif c == 'remove':
        S.discard(int(lst[1]))
    elif c == 'check':
        if int(lst[1]) in S:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        if int(lst[1]) in S:
            S.remove(int(lst[1]))
        else:
            S.add(int(lst[1]))
    elif c == 'all':
        S = set([i for i in r(1, 21)])
    elif c == 'empty':
        S.clear()