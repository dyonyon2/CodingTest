# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13

# 풀이 1 : 약수 구하는 방식으로 처리. 숫자 i*j는 i,j의 약수를 가지고 있기에 해당 숫자는 소수가 아님으로 판단 (17425번 문제 참고)
# MAX = 1000000
# array = [True]*(MAX+1)
# array[0] = False
# array[1] = False

# for i in range (2,MAX+1):
#     j = 2
#     while i*j <= MAX:
#         array[i*j] = False
#         j+=1

# a,b = map(int,input().split())

# for i in range (a,b+1):
#     if array[i]==True:
#         print(i)

# 풀이 2 : 에라토스테네스의 체 (소수 구하기) 방법으로 해결. 자연수 N이 소수인지 검사(나누어 떨어지는 것이 있는지)할 때에는 2부터 N의 제곱근까지만 확인하면 된다. 그 이후는 의미가 없다는 것이 에라토스테네스의 체
import math
a, b = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    sq = int(math.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
    
for i in range(a,b+1):
    if isPrime(i):
        print(i)