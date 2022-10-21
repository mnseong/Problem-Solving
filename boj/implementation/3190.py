'''
삼성전자 SW 역량테스트 > "뱀"
"https://www.acmicpc.net/problem/3190"
'''

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

# 맵 정보
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # 사과가 있는 위치는 1로 표시
board[0][0] = 2  # 뱀이 있는 위치는 2로 표시

# 방향 회전 정보 입력
l = int(input())
commands = [tuple(input().split()) for _ in range(l)]

# 처음에 동쪽을 보고 있음, 방향 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 회전 함수
def turn(direction, command):
    direction = (direction - 1) % 4 if command == 'L' else (direction + 1) % 4
    return direction


# 시뮬레이션 함수
def simulate():
    x, y = 0, 0
    d, i = 0, 0  # 방향, 다음에 회전할 정보
    info = [(0, 0)]  # 뱀이 차지하고 있는 위치 정보
    ret = 0  # 흐른 시간

    # 맵 밖으로 벗어나거나, 머리가 몸통을 만날 때 까지 반복
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                info.append((nx, ny))
                px, py = info.pop(0)
                board[px][py] = 0
            elif board[nx][ny] == 1:
                board[nx][ny] = 2
                info.append((nx, ny))
        else:
            ret += 1
            break
        ret += 1
        x, y = nx, ny

        # 회전 타이밍
        if i < l and ret == int(commands[i][0]):
            d = turn(d, commands[i][1])
            i += 1
    return ret


print(simulate())