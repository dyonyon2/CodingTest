# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은  A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4

# 풀이 1: 부분수열을 순서를 변경해서 만들어도 된다고 생각했는데.... 그것이 아닌가봄....;; =>  부분수열의 나열은 원래 수열의 반복이나 역순이 허용되지 않는다.

# import sys
# input = sys.stdin.readline

# count = int(input())
# array = list(map(int,input().split()))
# array.sort()
# print(array)
# standard = array[0]
# max = 1

# for i in range(1,count):
#     if standard<array[i]:
#         max+=1
#     standard = array[i]
# print(max)

# 풀이 2 : 

import sys
input = sys.stdin.readline

count = int(input())
array = list(map(int,input().split()))
dp = [1 for _ in range(count)]
for i in range(1,count):
    for j in range(i):
        if array[i]>array[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))