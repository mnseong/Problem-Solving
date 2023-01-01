"""
"별 찍기 - 11"
"https://www.acmicpc.net/problem/2448"
"""

import sys
input = sys.stdin.readline

n = int(input())

# 삼각형이 그려질 전체 테이블
stars = [[' '] * 2 * n for _ in range(n)]

def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j + 1] = stars[i + 1][j - 1] = '*'
        
        for k in range(5):
            stars[i + 2][j - (k - 2)] = '*'
    else:
        new_size = size // 2
        recursion(i, j, new_size)
        recursion(i + new_size, j - new_size, new_size)
        recursion(i + new_size, j + new_size, new_size)

recursion(0, n - 1, n)

for star in stars:
    print(''.join(star))
