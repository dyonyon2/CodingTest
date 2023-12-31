# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.

# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

# 입력의 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

# 예제 입력 1 
# 8
# 20
# 42
# 0
# 예제 출력 1 
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

# 풀이 1 : 숫자를 입력 받고 그 밑 숫자들중 소수인 것을 구한다. 소수들중 작은 숫자부터 꺼내어 위 조건이 만족하는지 확인한다 => 시간 초과
# while True:
#     num = int(input())
#     lst = []

#     # 0 입력시 종료
#     if num == 0:
#         break

#     # Num 보다 작은 소수 구하기
#     for i in range(2,num-1): # i 가 소수인가?
#         flag = True
#         for j in range(2,i+1):
#             if i%j==0 and i!=j:
#                 flag = False
#                 break
#         if flag==True: # i가 소수일 때 list에 추가
#             lst.append(i)

#     for tmp1 in lst: #lst를 돌면서 제일 작은 소수 값부터 문제의 조건이 성립하는 쌍을 찾는다.
#         tmp2 = num - tmp1
#         if tmp2 in lst:
#             print(num," = ",tmp1," + ",tmp2)
#             break

# 풀이 2 : 미리 소수를 구한 뒤(에라토스테네스의 체 or 약수 구하는 방식), 입력을 받고 조건을 만족하는지 확인한다.
# 풀이 2-1 : 약수 구하는 방식 => 시간 초과
# MAX = 1000000
# array = [True]*(MAX+1)

# array[0] = False
# array[1] = False
# for i in range (2,MAX+1):
#     j = 1
#     while i*j<=MAX:
#         if j!=1:
#             array[i*j] = False
#         j+=1

# while True:
#     num = int(input())
#     for tmp1 in range(2,num): #lst를 돌면서 제일 작은 소수 값부터 문제의 조건이 성립하는 쌍을 찾는다.
#         if array[tmp1] == True:
#             tmp2 = num - tmp1
#             if array[tmp2]==True:
#                 print(num," = ",tmp1," + ",tmp2)
#                 break

# 풀이 2-2 : 에라토스테네스의 체  => 시간 초과
# import math
# MAX = 1000000
# array = [True]*(MAX+1)

# array[0] = False
# array[1] = False
# for i in range (2,MAX+1):
#     for j in range (2,int(math.sqrt(i))+1):
#         if i%j==0 and i!=j:
#             array[i] = False

# while True:
#     num = int(input())
#     for tmp1 in range(2,num): #lst를 돌면서 제일 작은 소수 값부터 문제의 조건이 성립하는 쌍을 찾는다.
#         if array[tmp1] == True:
#             tmp2 = num - tmp1
#             if array[tmp2]==True:
#                 print(num," = ",tmp1," + ",tmp2)
#                 break

# 풀이 2-3 : 에라토스테네스의 체 다른 방식으로 사용. 하나의 숫자의 제곱근까지만 검사해도 된다는 것 = 그 숫자까지의 모든 숫자가 제곱근 밑 숫자의 배수로 소수가 걸러진다는 뜻
import math

MAX = 1000000
# array = [True] * (MAX+1)
array = [True for _ in range(MAX+1)]

array[0] = False
array[1] = False
for i in range (2,int(math.sqrt(MAX))+1):
# for i in range (2,int(MAX**0.6)):
    if array[i] == True:
        for j in range (i+i,MAX+1,i):
            if array[j] == True:
                array[j] = False

import sys
input = sys.stdin.readline

while True:
    num = int(input())
    if num == 0:
        break
    for tmp1 in range(3,num): #lst를 돌면서 제일 작은 소수 값부터 문제의 조건이 성립하는 쌍을 찾는다.
        if array[tmp1] == True:
            if array[num - tmp1]==True:
                # print("%d = %d + %d"%(num , tmp1 , num - tmp1))
                # print(num,"=",tmp1,"+",num - tmp1)
                break