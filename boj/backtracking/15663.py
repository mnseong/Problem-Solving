"""
"N과 M (9)"
"https://www.acmicpc.net/problem/15663"
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
    for i in range(n):
        if check[i] == 1: continue
        arr.append(numbers[i])
        check[i] = 1
        backtracking(arr, i + 1)
        arr.pop()
        check[i] = 0


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

hash_list = {}
check = [0] * n

numbers.sort()
backtracking([], 0)
