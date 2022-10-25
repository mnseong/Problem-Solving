'''
2020 KAKAO BLIND RECRUITMENT > "자물쇠와 열쇠"
"https://programmers.co.kr/learn/courses/30/lessons/60059"
'''


# 2차원 list를 시계방향으로 90도 회전시키는 함수
def rotation_90(a):
    return list(zip(*a[::-1]))


# key와 lock이 맞물리는지 확인하는 함수
def check(a, m, n):
    for i in range(n):
        for j in range(n):
            if a[m + i][m + j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)

    # 완전 탐색을 위해 lock확장 (ex_lock)
    k = 2 * m + n
    ex_lock = [[0] * k for _ in range(k)]

    # ex_lock중앙에 lock의 요철값 입력
    for i in range(n):
        for j in range(n):
            ex_lock[m + i][m + j] = lock[i][j]

    # 네 가지 방향에 대해 완전 탐색
    for _ in range(4):
        key = rotation_90(key)
        for x in range(1, m + n):
            for y in range(1, m + n):
                for i in range(m):
                    for j in range(m):
                        ex_lock[x + i][y + j] += key[i][j]
                if check(ex_lock, m, n) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        ex_lock[x + i][y + j] -= key[i][j]
    return False
