'''
"트리의 지름"
"https://www.acmicpc.net/problem/1967"
'''

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
 
def dfs(v):
    done[v] = True
    for i in range(n):
        if graph[v][i] and not done[i]:
            dfs(i)

n = int(input())
m = int(input())
count = 0

graph = [[0] * n for _ in range(n)]
done = [False] * n
for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1], graph[y-1][x-1] = 1, 1

dfs(0)
for i in done:
    if i:
        count += 1

print(count-1)