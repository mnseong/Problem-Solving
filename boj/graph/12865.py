'''
"평범한 배낭"
"https://www.acmicpc.net/problem/12865"
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(k+1)]

for w, v in items:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)
        
print(dp[-1])
