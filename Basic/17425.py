# 문제
# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)가 주어진다. 둘째 줄부터 테스트 케이스가 한 줄에 하나씩 주어지며 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.

# 예제 입력 1 
# 5
# 1
# 2
# 10
# 70
# 10000
# 예제 출력 1 
# 1
# 4
# 87
# 4065
# 82256014

# 풀이 1 : 17427번 문제와 같이 1~N 자연수의 각 약수의 합은 소수가 아님으로 판단 => 시간 초과
# count = int(input())
# for i in range(1,count+1):
#     num = int(input())
#     sum = 0
#     for j in range(1,num+1):
#         sum = sum + num//j*j
#     print(sum)


#풀이 2 : 숫자(i*j)는 i와 j의 곱으로 이루이진 숫자이므로, i와 j를 약수로 가진다. i와 j를 증가시키며 i를 약수에 포함시킨다. 사용자 입력 전 규칙을 통해 미리 값을 만들어 처리한다.
import sys

MAX = 1000000
F_Array = [0] * (MAX+1)
G_Array = [0] * (MAX+1)

for i in range (1, MAX+1):
    j = 1
    while i*j <= MAX:
        F_Array[i*j] += i
        j+=1
    G_Array[i] = G_Array[i-1] + F_Array[i]

count = int(input())

for _ in range(count):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(G_Array[a])+"\n")