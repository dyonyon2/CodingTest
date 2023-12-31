# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

# 예제 입력 1 
# 3
# CCP
# CCP
# PPC
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# PPPP
# CYZY
# CCPY
# PPCC
# 예제 출력 2 
# 4
# 예제 입력 3 
# 5
# YCPZY
# CYZZP
# CCPPP
# YCYZC
# CPPZZ
# 예제 출력 3 
# 4

import sys
input = sys.stdin.readline

global ans
ans = 0
line=int(input())
array = [[0]*line for _ in range(line)]

def check(a,b):
    # 행 체크
    count = 1
    max = 0
    global ans
    for i in range(line):
        if i == 0:
            prev = array[a][i]
        elif prev == array[a][i]:
            count+=1
            if count>max:
                max = count
        else:
            count = 1
        prev = array[a][i]
    if ans < max : 
        ans = max


    # 열 체크
    count = 1
    max = 0
    for i in range(line):
        if i == 0:
            prev = array[i][b]
        elif prev == array[i][b]:
            count+=1
            if count>max:
                max = count
        else:
            count = 1
        prev = array[i][b]
    if ans < max : 
        ans = max

# 처리 => 순서 변경 -> 체크 -> 순서 초기화
def process(a,b):
    if a+1<line:
        array[a][b], array[a+1][b] = array[a+1][b], array[a][b]
        check(a,b)
        check(a+1,b)
        array[a][b], array[a+1][b] = array[a+1][b], array[a][b]
    if b+1<line:
        array[a][b], array[a][b+1] = array[a][b+1], array[a][b]
        check(a,b)
        check(a,b+1)
        array[a][b], array[a][b+1] = array[a][b+1], array[a][b]

# 입력 받기
for i in range(line):
    colors = input()
    for j in range(len(colors)-1):
        array[i][j] = colors[j]

# 처리
for i in range(line):
    for j in range(line):
        process(i,j)
print(ans)