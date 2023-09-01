# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

# ㅣ ㅣ ㅡㅡ ㅣ
# ㅣ ㅣ ㅡㅡ ㅣ

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 9
# 예제 출력 2 
# 55

# 풀이 : 규칙을 찾아 DP

# array[0] = 0
# array[1] = 1
# array[2] = 2
# array[3] = 3
# array[4] = 5
# array[5] = 8


import sys
input = sys.stdin.readline

n = int(input())

array = [ 0 for _ in range(n+1)]
array[1] = 1
if n > 1:
    array[2] = 2

for i in range(3,n+1):
    array[i] = array[i-1]+array[i-2]

print(array[n]%10007)
