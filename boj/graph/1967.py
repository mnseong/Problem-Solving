'''
"트리의 지름"
"https://www.acmicpc.net/problem/1967"
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree: dict = {i: set() for i in range(n+1)}  # {vertex: {(num, weight), ...}}
for i in range(n-1):
    p, c, w = map(int, input().split())  # parent, child, weight
    tree[p].add((c, w))
    tree[c].add((p, w))

def bfs(start: int) -> list:
    queue = deque()
    queue.append((start, 0))
    visited = (n+1)*[0]
    visited[start] = 1
    res = [0, 0]  # [시작점에서부터의 최대 가중치를 가진 노드, 가중치]
    
    while queue:
        cur, tmp = queue.popleft()
        for i in tree[cur]:
            v, e = i[0], i[1]
            if visited[v] == 0:
                visited[v] = 1
                queue.append([v, tmp + e])
                if res[1] < tmp + e:
                    res[0] = v
                    res[1] = tmp + e

    return res

print(bfs(bfs(1)[0])[1])