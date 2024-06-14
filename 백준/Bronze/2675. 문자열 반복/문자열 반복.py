t = int(input())
# result = ''
for _ in range(t):
    num, s = input().split()
    for i in range(len(s)):
        # result += s[i]*int(num)
        print(s[i]*int(num), end='')
    print()
# print(result)