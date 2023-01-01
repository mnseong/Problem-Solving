"""
"N과 M (12)"
"https://www.acmicpc.net/problem/15666"
"""

import sys
input = sys.stdin.readline

def backtracking(arr, idx):
    if len(arr) == m:
        s = ' '.join(map(str, arr))
        if s not in hash_list:
            hash_list[s] = 1
            print(s)
        return
    for i in range(idx, n):
        arr.append(numbers[i])
        backtracking(arr, i)
        arr.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

hash_list = {}

numbers.sort()
backtracking([], 0)
