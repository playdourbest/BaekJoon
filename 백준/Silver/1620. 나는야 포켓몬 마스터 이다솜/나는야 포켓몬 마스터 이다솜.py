# 첫째줄 : N(포켓몬 수), M(맞춰야 하는 수)
# 둘째줄 ~ N : 이름이 각 줄에 입력, 모두 영어
# M ~ : 이름입력 -> 번호출력 ; 번호입력 -> 이름 출력

# (런타임 에러)
# 리스트 한개 만들어서 번호로 이름 찾기 구현하기
# 딕셔너리 한개 만들어서 이름으로 번호찾기 구현하기

# 딕셔너리 한개 만들어서 위 두개 한번에 구현하기

import sys
r=range;input=sys.stdin.readline
N, M = map(int, input().split())

# jupyter 에선 작동하나 백준에선 런타임에러 발생.
# pokemon_list = []
# pokemon_dict = {}

# for i in r(1, N+1):
#     name = input().rstrip()
#     pokemon_list.append(name)
#     pokemon_dict[name] = i

# for _ in r(M):
#     query = input()
#     if query.isdigit():
#         print(pokemon_list[int(query) - 1])
#     else:
#         print(pokemon_dict[query])

pokemon_dict = {}
for i in r(1, N+1):
    name = input().rstrip()
    pokemon_dict[i] = name
    pokemon_dict[name] = i

for _ in r(M):
    query = input().rstrip()
    if query.isdigit():
        print(pokemon_dict[int(query)])
    else:
        print(pokemon_dict[query])