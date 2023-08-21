# 문제
# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

# 입력
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

# 출력
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

# 예제 입력 1 
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
# 예제 출력 1 
# 7
# 8
# 10
# 13
# 19
# 20
# 23

# 풀이 : 입력 받아서 정렬한 뒤, 2개씩 골라서 diff와 같으면 pop
import sys
input = sys.stdin.readline
array = []
sum = 0

for i in range(9):
    array.append(int(input()))
    sum += array[i]
diff = sum - 100

# print(array)
# print(sum)
# print(diff)

# 버블 정렬
for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
# python은 배열 정렬 제공함 => sort()
# array.sort()
# print(array)

for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==diff:
            array.pop(i)
            array.pop(j-1)
            for k in range(len(array)):
                print(array[k])
            sys.exit()
            



# 풀이 2 : 재귀방법
short_men = [int(input()) for _ in range(9)]
seven_short_temp = []  # 7명을 뽑아 합을 조사할 새로운 리스트 선언


def dfs(depth, start):
    if depth == 7:  # 만약 7번 재귀를 돌았다면
        if sum(seven_short_temp) == 100:  # 현재 저장된 일곱난쟁이들의 합이 100이라면
            for j in sorted(seven_short_temp):  # 오름차순으로 정렬 후 출력
                print(j)
            exit()  # 그 후 코드 종료
        else:  # 만약 7명을 뽑았는데 합이 100이 아니라면
            return  # 해당 재귀를 더이상 실행하지 않고 종료

    for i in range(start, len(short_men)):  # 시작인덱스와 9명의 난쟁이가 있으므로 9번을 돈다.
        seven_short_temp.append(short_men[i])  # 난쟁이 한명을 추가한다.
        dfs(depth + 1, i + 1)  # dfs를 돈다(다음번 깊이는 +1로 해주고 인덱스는 중복되지 않게 하기위해서 다음 인덱스를 넣어준다.)
        seven_short_temp.pop()  # dfs를 돌다 7명이 다 찼으나 합이 100이 아니어서 return 되었으면 넣었던 난쟁이 한명을 다시 빼준다.


dfs(0, 0)  # dfs를 돈다.