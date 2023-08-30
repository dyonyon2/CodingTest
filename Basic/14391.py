# 문제
# 영선이는 숫자가 쓰여 있는 직사각형 종이를 가지고 있다. 종이는 1×1 크기의 정사각형 칸으로 나누어져 있고, 
# 숫자는 각 칸에 하나씩 쓰여 있다. 행은 위에서부터 아래까지 번호가 매겨져 있고, 열은 왼쪽부터 오른쪽까지 번호가 매겨져 있다.

# 영선이는 직사각형을 겹치지 않는 조각으로 자르려고 한다. 각 조각은 크기가 세로나 가로 크기가 1인 직사각형 모양이다. 
# 길이가 N인 조각은 N자리 수로 나타낼 수 있다. 가로 조각은 왼쪽부터 오른쪽까지 수를 이어 붙인 것이고, 세로 조각은 위에서부터 아래까지 수를 이어붙인 것이다.

# 아래 그림은 4×4 크기의 종이를 자른 한 가지 방법이다.



# 각 조각의 합은 493 + 7160 + 23 + 58 + 9 + 45 + 91 = 7879 이다.

# 종이를 적절히 잘라서 조각의 합을 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 종이 조각의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 4)

# 둘째 줄부터 종이 조각이 주어진다. 각 칸에 쓰여 있는 숫자는 0부터 9까지 중 하나이다.

# 출력
# 영선이가 얻을 수 있는 점수의 최댓값을 출력한다.

# 예제 입력 1 
# 2 3
# 123
# 312
# 예제 출력 1 
# 435
# 예제 입력 2 
# 2 2
# 99
# 11
# 예제 출력 2 
# 182
# 예제 입력 3 
# 4 3
# 001
# 010
# 111
# 100
# 예제 출력 3 
# 1131
# 예제 입력 4 
# 1 1
# 8
# 예제 출력 4 
# 8

# 풀이 1 : 4칸이면 4칸을 다 사용하는게 가장 큰 숫자라고 가정 -> 세로 쭉 합과 가로 쭉 합 계산 => 실패....   ==>> 비트마스크 기법 공부!

# import sys
# input = sys.stdin.readline

# N,M = map(int,input().split())
# array = [[0 for _ in range(M)] for i in range(N)]
# for i in range(N):
#     num = int(input())
#     array[i] = list(map(int,str(num).zfill(M)))
# max = 0
# tmp = 0

# # 가로 계산
# for i in range(N):
#     for j in range(M):
#         if array[i][j]!=0:
#             tmp = tmp + array[i][j]*(10**((M-1)-j))
# max = tmp

# # 세로 계산
# tmp = 0
# for j in range(M):
#     for i in range(N):
#         if array[i][j]!=0:
#             tmp = tmp + array[i][j]*(10**((N-1)-i))
# if tmp>max:
#     max = tmp

# print(max)


# 풀이 2 : 비트 마스크 기법을 통하여, 모든 경우의 수를 계산하는 방식

import sys

input = sys.stdin.readline

# n행, m열
n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))

ans = []

for case in range(1 << n*m):
    total = 0
    # 가로는 0
    for row in range(n):
        rowsum = 0
        for col in range(m):
            now = row*m+col
            if case & (1<<now) == 0: # 가로일 때
                rowsum = rowsum * 10 + paper[row][col]
            else: # 세로일 때
                total += rowsum
                rowsum = 0
        total += rowsum
    
    # 세로는 1
    for col in range(m):
        colsum = 0
        for row in range(n):
            now = row*m+col
            if case & (1<<now) != 0: # 세로일 때
                colsum = colsum * 10 + paper[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    
    ans.append(total)

print(max(ans))