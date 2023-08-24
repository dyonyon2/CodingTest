# 문제
# 크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 
# 이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다. 
# 단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, 
# (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

# 입력
# 첫째 줄에 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에 격자판에 들어있는 수가 주어진다.

# 출력
# 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 출력한다.

# 제한
# 1 ≤ N, M ≤ 10
# 1 ≤ K ≤ min(4, N×M)
# 격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
# 항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.
# 예제 입력 1 
# 1 1 1
# 1
# 예제 출력 1 
# 1
# 예제 입력 2 
# 2 2 2
# 1 2
# 3 4
# 예제 출력 2 
# 5
# 예제 입력 3 
# 2 2 2
# 5 4
# 4 5
# 예제 출력 3 
# 10
# 예제 입력 4 
# 5 5 3
# 1 9 8 -2 0
# -1 9 8 -3 0
# -5 1 9 -1 0
# 0 0 0 9 8
# 9 9 9 0 0
# 예제 출력 4 
# 27

# 풀이 1 : [i][j] 2중 for 문으로 전체 돌면서 모든 값 확인 => 시간 초과

import sys
input = sys.stdin.readline

row,col,count = map(int,input().split())
array = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    array[i] = list(map(int,input().split()))
result = []
visited = [[False for _ in range(col)] for _ in range(row)]
max = 0

def dfs():
    if len(result) == count:
        global max
        if max < sum(result):
            max = sum(result)
        return
    for i in range(row):
        for j in range(col):
            if len(result) != 0:
                if visited[i][j] == True : continue
                if i-1>=0: 
                    if visited[i-1][j] == True: continue
                if i+1<row: 
                    if visited[i+1][j] == True: continue
                if j-1>=0: 
                    if visited[i][j-1] == True: continue
                if j+1<col: 
                    if visited[i][j+1] == True: continue
            visited[i][j] = True
            result.append(array[i][j])
            dfs()
            result.pop()
            visited[i][j] = False
dfs()
print(max)