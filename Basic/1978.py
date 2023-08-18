# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1 
# 4
# 1 3 5 7
# 예제 출력 1 
# 3

# 풀이 : 주어진 수를 반복문을 돌아 나누어서 자신과 1을 제외한 다른 약수가 있을시에는 소수가 아닌 것으로 판단! 예외처리 집중(1이상, 1&자기자신 제외)

count = int(input())
lst = list(map(int, input().split()))
sum = 0

for i in lst:
    if i >1:
        flag = True
        for j in range(2,i+1):
            if i%j==0 and i>1 and i!=j: #소수가 아닌 경우
                flag = False
                break
        if flag == True:
            sum+=1
            
print(sum)