"""
"평범한 배낭"
"https://www.acmicpc.net/problem/12865"
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cargo = [tuple(map(int, input().split())) for i in range(n)]

pack = []
for i in range(len(cargo) + 1):
    pack.append([])
    for c in range(k + 1):
        if i == 0 or c == 0:
            pack[i].append(0)
        elif cargo[i-1][0] <= c:
            pack[i].append(
                max(
                    cargo[i-1][1] + pack[i-1][c-cargo[i-1][0]],
                    pack[i-1][c]
                )
            )
        else:
            pack[i].append(pack[i-1][c])

print(pack[-1][-1])
