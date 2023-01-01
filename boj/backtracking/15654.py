"""
"N과 M (5)"
"https://www.acmicpc.net/problem/15654"
"""

import sys
input = sys.stdin.readline

def backtracking(arr, idx):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        if numbers[i] in arr: continue
        arr.append(numbers[i])
        backtracking(arr, i + 1)
        arr.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
backtracking([], 0)
