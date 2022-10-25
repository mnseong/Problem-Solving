'''
이코테 > chapter 05 > "음료수 얼려먹기"
by BFS
'''


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]  # 공백없이 입력받을 때 주의...
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 너비 우선 탐색
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return True


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        else:
            bfs(i, j)
            cnt += 1

print(cnt)
