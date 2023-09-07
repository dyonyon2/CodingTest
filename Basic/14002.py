# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4
# 10 20 30 50
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
result = [1 for _ in range(N)]
index = [-1 for _ in range(N)]
result_array = []

for i in range(1,N):
    tmp = -1
    for j in range(0,i):
        if array[j]<array[i]:
            if result[i]<result[j]+1:
                result[i] = result[j]+1
                tmp = j
    index[i] = tmp
print(max(result))
tmp = result.index(max(result))
while True:
    if tmp == -1:
        break
    result_array.append(array[tmp])
    tmp = index[tmp]
result_array.reverse()
print(' '.join(map(str,result_array)))