# 문제
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

# 입력
# 첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

# 출력
# 첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 20 2
# 예제 출력 1 
# 21
# 예제 입력 2 
# 6 4
# 예제 출력 2 
# 84


# 풀이 1: BF 방식 => 아마 시간초과 뜰거임... => 시간 초과

# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())
# result = []
# count = 0

# def bf():
#     global count
#     if len(result)==K:
#         if sum(result)==N:
#             print(result)
#             count += 1
#         return
    
#     for i in range(N+1):
#         result.append(i)
#         bf()
#         result.pop()

# bf()
# print(count)

# 풀이 2 : DP 방식...

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]
for i in range(1,201):
    dp[0][i] = 1
    dp[i][1] = 1

for i in range(201):
    for j in range(201):
        if i-1>=0 and j-1>=0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000

print(dp[N][K])