# 4 3 6 8 7 5 2 1

# 1. 4 -> 4가 push 되어야함. 따라서 1,2,3,4 값이 스택에 있다는 의미(push 4번). 그 후 4를 pop
# [push, push, push, push, pop]

# 2. 3 -> 1,2,3 이 남아있고 3이 가장 큰값이기 때문에 그대로 3을 pop.
# [pop]

# 3. 6 -> 6 이 push 되어야함. 따라서 6보다 작은 값들이 스택에 있어야함.
#                 즉, 5,6 이 push(push 2번). 스택엔 1,2,5,6 있음. 그 후 6 pop
# [push, push, pop]

# 4. 8 -> 8보다 작은 값들을 push. 스택엔 1,2,5,6,7,8(push 2번) 그 후 8 pop
# [push, push, pop]

# 5. 7 -> 스택에 있으니 그대로 pop
# [pop]

# 6. 이하 5번과 동일한 과정으로 pop 만 진행

import sys
n=int(sys.stdin.readline().strip())
result,stack,cur = [],[],1

for _ in range(n):
  seq = int(sys.stdin.readline().strip())
  while cur <= seq:
    stack.append(cur)
    result.append('+')
    cur += 1
  if stack[-1] == seq:
    stack.pop()
    result.append('-')
  else:
    result.clear()
    result.append('NO')
    break
for answer in result:
  print(answer)