"""
"행렬 곱셈 순서"
"https://www.acmicpc.net/problem/11049"
"""

import sys
input = sys.stdin.readline

n = int(input())

matrix_list = [()]
dp = [[0 for i in range(n+2)] for i in range(n+2)]

for _ in range(n):
    r, c = map(int, input().split())
    matrix_list.append((r, c))

for i in range(1, n):
    for j in range(1, n-i+1):
        dp[j][i+j] = 2**31 - 1
        for k in range(j, i+j+1):
            dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + matrix_list[j][0] * matrix_list[k][1] * matrix_list[i+j][1])

print(dp[1][n])
