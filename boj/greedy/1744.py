'''
BOJ 1744번 수 묶기
https://www.acmicpc.net/problem/1744
'''

import sys
input = sys.stdin.readline

positive, negative = [], []
answer = 0

n = int(input())
for _ in range(n):
    x = int(input())
    if x > 1:
        positive.append(x)
    elif x <= 0:
        negative.append(x)
    
    # 입력값이 1이면 바로 answer에 더해줌
    else:
        answer += 1

# 양수 list는 내림차순
positive.sort(reverse = True)

# 음수 list는 오름차순
negative.sort()

# 양수의 개수가 짝수라면, 앞에서 부터 2개씩 묶어 곱해서 더함
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        answer += positive[i] * positive[i+1]

# 양수의 개수가 홀수라면, 앞에서 부터 2개씩 묶어 곱해서 더하고, 마지막 남은 하나는 그냥 더함
else:
    for i in range(0, len(positive)-1, 2):
        answer += positive[i] * positive[i+1]
    answer += positive[len(positive)-1]

# 음수도 양수와 마찬가지로 처리
if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        answer += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        answer += negative[i] * negative[i+1]
    answer += negative[len(negative)-1]

print(answer)