"""
"트리의 부모 찾기"
"https://www.acmicpc.net/problem/11725"
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

isVisited = [False] * (n + 1)
tree = {x: [] for x in range(n + 1)}
ans = {x: [] for x in range(n + 1)}

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)


def dfs(node):
    isVisited[node] = True
    for x in tree[node]:
        if not isVisited[x]:
            dfs(x)
            ans[x] = node


dfs(1)

for x in range(2, n + 1):
    print(ans[x])
