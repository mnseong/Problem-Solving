"""
"N과 M (4)"
"https://www.acmicpc.net/problem/15652"
"""

import sys
input = sys.stdin.readline

def dfs(arr, idx):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(idx, n):
        arr.append(numbers[i])
        dfs(arr, i)
        arr.pop()


n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
dfs([], 0)
