# 입력된 값을 sorted 해주고 딕셔너리에 저장
# 딕셔너리에 저장된 값을 순서대로 번호 부여
# 입력된 값에 대해서 번호 출력

import sys
input=sys.stdin.readline
def baekjoon_18870(N, num):
    lst = sorted(set(num))
    map_dict = {instance: index for index, instance in enumerate(lst)}
    output = [map_dict[x] for x in num]
    return output

N = int(input())
num = list(map(int, input().split()))

print(' '.join(map(str, baekjoon_18870(N, num))))

# for result in baekjoon_18870(N, num):
#     print(result, end=' ')