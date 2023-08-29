# 문제
# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

# 예제 입력 1 
# 4
# 1 2 3 4
# 예제 출력 1 
# 1 2 4 3
# 예제 입력 2 
# 5
# 5 4 3 2 1
# 예제 출력 2 
# -1

# 풀이 1 : DFS 브루트포스로는 시간 초과 발생 
# import sys
# input = sys.stdin.readline

# maxNum = int(input())
# tmp = list(map(int,input().split()))
# step = []
# flag = False

# def check():
#     global flag
#     if step == tmp:
#         flag = True
#     elif flag:
#         print(' '.join(map(str,step)))
#         flag = False
#         exit(0)

# def process():
#     if len(step) == maxNum:
#         check()
#         return
    
#     for i in range(1,maxNum+1):
#         if i not in step:
#             step.append(i)
#             process()
#             step.pop()

# process()
# if flag:
#     print("-1")

# 풀이 2 : 규칙 찾기
import sys
input = sys.stdin.readline

maxNum = int(input())
result = list(map(int,input().split()))
step = []

def findIndex():
    for i in range(maxNum-1,0,-1):
        if result[i-1] < result[i]:
            return i-1
    return -100

def findLessValue(index):
    global result
    for i in range(maxNum-1,index,-1):
        if result[index] < result[i]:
            result[index], result[i] = result[i], result[index]
            return

index = findIndex()
if index==-100:
    print(-1)
else:
    findLessValue(index)
    result = result[:index+1] + sorted(result[index+1:])
    print(' '.join(map(str,result)))

