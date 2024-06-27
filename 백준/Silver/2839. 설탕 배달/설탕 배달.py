# 3Kg 과 5Kg 을 조합
# 3의 배수 + 5의 배수 -> 이 값들은 모두 가능
# 5의 배수로 먼저 빼주고 그다음 3의 배수로 빼지는지 확인
# ex)18 -> 5의 배수(15)로 빼고 3의 배수로 뺌
import sys
input=sys.stdin.readline
n=int(input());p=0
while n%5:
    n-=3;p+=1
print(-1 if n<0 else p+n//5)