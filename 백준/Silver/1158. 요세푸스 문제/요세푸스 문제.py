import sys
input=sys.stdin.readline

def baekjoon_1158(N, K):
    people = list(range(1, N+1))
    result = []
    index = 0
    while people:
        index = (index + K - 1) % len(people)  # K번째 사람의 인덱스 계산
        result.append(people.pop(index))  # 사람 제거하고 결과에 추가
    return result

N, K = map(int, input().split())
print(f"<{', '.join(map(str, baekjoon_1158(N, K)))}>")