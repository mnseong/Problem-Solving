'''
위클리 챌린지
"https://school.programmers.co.kr/learn/courses/30/lessons/82612"
'''

def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(count):
        total += price * (i + 1)
    answer = total - money

    return 0 if answer <= 0 else answer