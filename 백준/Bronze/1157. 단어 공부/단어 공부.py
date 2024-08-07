from collections import Counter
import sys
input=sys.stdin.readline

def baekjoon_1157(word):
    word = word.upper()
    count = Counter(word)
    cnt = max(count.values())
    most = [letter for letter, freq in count.items() if freq == cnt]
    if len(most) > 1:
        return '?'
    else:
        return most[0]

word = input().strip()
print(baekjoon_1157(word))