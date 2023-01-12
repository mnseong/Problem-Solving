'''
월간 코드 챌린지 - 음양 더하기
"https://school.programmers.co.kr/learn/courses/30/lessons/76501"
'''

def solution(absolutes, signs):
    for i in range(len(signs)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)