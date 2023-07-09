"""
"집합의 표현"
"https://www.acmicpc.net/problem/1717"
"""

import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a == b:
        return
    p, c = min(a, b), max(a, b)
    parent[c] = p


def find_parent(a, b):
    return 'YES' if get_parent(a) == get_parent(b) else 'NO'


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b)
    else:
        print(find_parent(a, b))
