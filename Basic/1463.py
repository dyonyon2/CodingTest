# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10
# 예제 출력 2 
# 3

# 풀이 1 : 모든 Case 다 돌기 => 시간 초과

# import sys
# input = sys.stdin.readline

# num = int(input())
# min = 1000

# def dp(num, count):
#     if num == 1:
#         global min
#         if count < min:
#             min = count
#         return
#     for i in range(3):
#         if i == 0:
#             if num%3==0:
#                 num = num/3
#                 count += 1
#                 dp(num,count)
#                 num = num * 3
#                 count -= 1
#         elif i == 1:
#             if num%2==0:
#                 num = num/2
#                 count += 1
#                 dp(num,count)
#                 num = num * 2
#                 count -= 1
#         elif i == 2:
#             num = num - 1
#             count +=1
#             dp(num,count)
#             num = num + 1
#             count -= 1
        
# dp(num,0)
# print(min)


# 풀이 2 : 나누기 3 -> 나누기 2 -> 빼기 1 우선순위로 계산  => 반례 발생. 10은 1빼고 3으로 나누는게 최선이다.

# import sys
# input = sys.stdin.readline

# num = int(input())
# min = 1000

# def dp(num, count):
#     if num == 1:
#         global min
#         if count < min:
#             min = count
#         return
#     if num%3==0:
#         num = num/3
#         count += 1
#     elif num%2==0:
#         num = num/2
#         count += 1
#     else :
#         num = num - 1
#         count +=1
#     dp(num,count)
        
# dp(num,0)
# print(min)


# 풀이 3 : 다이나믹 프로그래밍 

import sys
input = sys.stdin.readline

num = int(input())
array = [0 for _ in range(num+1)]

for i in range(2,num+2):
    min = array[i-1] + 1
    tmp = min
    if i%3 == 0:
        tmp = array[i//3] + 1
        if tmp < min:
            min = tmp
    if i%2 == 0:
        tmp = array[i//2] + 1
        if tmp < min:
            min = tmp

print(array[num])
    