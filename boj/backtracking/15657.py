"""
"N과 M (8)"
"https://www.acmicpc.net/problem/15657"
"""

import sys
input = sys.stdin.readline

def backtracking(arr, idx):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(idx, n):
        arr.append(numbers[i])
        backtracking(arr, i)
        arr.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
backtracking([], 0)
