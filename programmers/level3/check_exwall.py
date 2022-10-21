'''
2020 KAKAO BLIND RECRUITMENT > "외벽 점검"
"https://programmers.co.kr/learn/courses/30/lessons/60062"
'''

# 순열 사용
from itertools import permutations


def solution(n, weak, dist):
    # weak list 길이를 2배로 늘리기 (원형자료를 선형자료로 바꾸어 생각)
    ex_weak = [(x + n) for x in weak]
    ex_weak = weak + ex_weak

    ret = len(dist) + 1  # 비교값 초기화

    # weak의 값을 차례대로 시작점으로 지정
    for s in range(len(weak)):
        for case in list(permutations(dist, len(dist))):
            need = 1  # 필요한 인력
            pos = ex_weak[s] + case[need - 1]  # 처음 사람이 확인할 수 있는 마지막 위치
            for i in range(s, s + len(weak)):
                if pos < ex_weak[i]:  # 현재 사람이 점검할 수 있는 범위 밖일 경우,
                    need += 1  # 인력 추가
                    if need > len(dist):  # 주어진 사람 수 보다 필요한 사람 수가 많은 경우
                        break  # -1을 반환하러 go
                    pos = ex_weak[i] + case[need - 1]  # 확인할 수 있는 마지막 위치 갱신
            ret = min(ret, need)

    if ret > len(dist):
        return -1
    else:
        return ret