# 문제
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

# 출력
# 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

# 예제 입력 1 
# 3
# 예제 출력 1 
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 풀이 1 : DFS로 for문 돌면서 하면 알아서 오름차순으로 실행됨
import sys
input = sys.stdin.readline

N = int(input())
count = 0
result = []

def fact(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return num * fact(num-1)

N_Fact = fact(N)

def dfs():
    if len(result) == N:
        global count
        count += 1
        print(' '.join(map(str,result)))
        if count == N_Fact:
            exit()

    for i in range(1,N+1):    
        if len(result) != 0:
            if i in result:
                continue
        result.append(i)
        dfs()
        result.pop()

dfs()