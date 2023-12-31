# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

# 1+2+1
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 3
# 4
# 7
# 10
# 예제 출력 1 
# 3
# 9
# 27


# 풀이 : 규칙을 찾아야함.... 이 문제는 1차원이 아니라 2차원적으로 규칙을 찾아야함..... 이걸 찾을수가 있나...? ;;

import sys
input = sys.stdin.readline
dp = [[0 for _ in range(3)] for i in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]
count = int(input())

for i in range(4,100001):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][0]+dp[i-2][2])%1000000009
    dp[i][2] = (dp[i-3][0]+dp[i-3][1])%1000000009

for _ in range(count):
    num = int(input())
    print(sum(dp[num])%1000000009)