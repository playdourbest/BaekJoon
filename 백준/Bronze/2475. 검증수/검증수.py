a = list(map(int, input().split()))

result = 0
for i in range(len(a)):
    result += (a[i]**2)
print(result%10)