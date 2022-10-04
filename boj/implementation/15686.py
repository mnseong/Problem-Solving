'''
삼성전자 SW 역량테스트 > "치킨 배달"
"https://www.acmicpc.net/problem/15686"
'''

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []

for r in range(n):
    for c in range(n):
        if city_map[r][c] == 1:
            house.append((r, c))
        elif city_map[r][c] == 2:
            chicken.append((r, c))

cases = list(combinations(chicken, m))  # 전체 치킨집 중에 m개를 뽑는 전체 경우
ret = 1e9

# 각 경우마다 확인하며 최소값 갱신
for case in cases:
    c_dist_c = 0  # chicken distance of city
    for hx, hy in house:
        c_dist = 1e9  # chicken distance
        for cx, cy in case:
            c_dist = min(c_dist, abs(hx - cx) + abs(hy - cy))
        c_dist_c += c_dist
    ret = min(ret, c_dist_c)

print(ret)