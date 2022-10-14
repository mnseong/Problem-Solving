'''
"특정 거리의 도시 찾기"
"https://www.acmicpc.net/problem/18352"
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 도로 별로 연결 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)  # 각 도시마다 최단거리 기록할 list
distance[x] = 0


# 너비 우선 탐색
def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                queue.append(node)


bfs(x)
if k not in distance:
    print(-1)
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)