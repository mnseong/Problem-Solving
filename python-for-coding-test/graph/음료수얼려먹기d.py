'''
이코테 > chapter 05 > "음료수 얼려먹기"
by DFS
'''


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]  # 공백없이 입력받을 때 주의...


# 깊이 우선 탐색
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    elif graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)
