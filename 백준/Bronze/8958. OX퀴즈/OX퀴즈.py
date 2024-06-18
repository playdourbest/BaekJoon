# n = int(input())
# score = 0
# score_sum = 0

# for _ in range(n):
#     ox = input()
#     for i in range(len(ox)):
#         if ox[i] == 'O':
#             score += 1
#         else:
#             score = 0
#         score_sum += score
#     print(score_sum)

n = int(input())

for i in range(n):
    ox = input()
    score = 0
    score_sum = 0
    for j in ox:
        if j == 'O':
            score += 1
        else:
            score = 0
        score_sum += score
    print(score_sum)