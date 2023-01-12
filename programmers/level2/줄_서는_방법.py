'''
연습문제 - 줄 서는 방법
"https://school.programmers.co.kr/learn/courses/30/lessons/12936"
'''

import math

def solution(n, k):
    answer = []
    arr = [x+1 for x in range(n)]
    
    for i in range(n, 0, -1):
        split_num = math.factorial(n-1)
        answer.append(arr[(k - 1) // split_num])
        arr.pop((k - 1) // split_num)
        k %= split_num
        n -= 1
    
    return answer