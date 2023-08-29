# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# 예제 입력 1 
# 6
# 20 1 15 8 4 10
# 예제 출력 1 
# 62

# 풀이 1 : DFS로 전체 확인. ** 배열 내의 정수가 값은 정수가 들어가 있을 수 있으니, visited로 index가 겹치는지만 확인!

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
result = []
visited = []
max = 0

def check():
    global max
    tmp = 0
    for i in range(N-1):
        tmp = tmp + abs(result[i]-result[i+1])
    if tmp > max:
        max = tmp

def dfs():
    if len(result)==N:
        check()
        return
    for i in range(N):
        if i not in visited:
            result.append(array[i])
            visited.append(i)
            dfs()
            result.pop()
            visited.pop()

dfs()
print(max)
