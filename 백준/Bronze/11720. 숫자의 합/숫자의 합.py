n = int(input())
x = list(map(int, input()))
out = 0
for i in range(n):
    out += x[i]
print(out)