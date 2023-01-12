"""
"플로이드"
"https://www.acmicpc.net/problem/11404"
"""

import sys
from math import inf

n = int(input())
m = int(input())

# cost 저장할 adjacency matrix
cost = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

for r in cost:
    for i in range(n):
        if r[i] == inf:
            r[i] = 0
        print(r[i], end=' ')
    print()
