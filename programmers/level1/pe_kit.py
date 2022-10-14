'''
"체육복"
"https://programmers.co.kr/learn/courses/30/lessons/42862"
'''


def solution(n, lost, reserve):
    common = set(lost) & set(reserve)  # 잃어버린 사람 중 여벌의 체육복이 있는 사람들
    lost = list(set(lost) - common)
    reserve = list(set(reserve) - common)
    for num in lost[:]:
        if num - 1 in reserve:
            lost.remove(num)
            reserve.remove(num - 1)
        elif num + 1 in reserve:
            lost.remove(num)
            reserve.remove(num + 1)
    return n - len(lost)