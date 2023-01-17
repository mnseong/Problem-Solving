"""
"외판원 순회"
"https://www.acmicpc.net/problem/2098"
"""

import sys
input = sys.stdin.readline
INF = 9876543210

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

def recursion(current, visited):
    if visited == (1 << n) - 1:
        if graph[current][0] == 0:
            return INF
        dp[current][visited] = graph[current][0]
        return graph[current][0]
    
    if dp[current][visited] != -1:
        return dp[current][visited]
    
    min_dist = INF
    
    for i in range(n):
        if not visited & (1 << i) and graph[current][i] != 0:
            min_dist = min(min_dist, graph[current][i] + recursion(i, visited | (1 << i)))
    
    dp[current][visited] = min_dist
    return min_dist

print(recursion(0, 1))
