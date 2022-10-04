'''
"ATM"
"https://www.acmicpc.net/problem/11399"
'''

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

for i in range(n - 1):
    p[i + 1] += p[i]

print(sum(p))