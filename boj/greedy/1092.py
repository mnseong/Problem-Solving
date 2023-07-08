'''
"배"
"https://www.acmicpc.net/problem/1092"
'''

import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

if crane[0] < box[0]:
    print(-1)
else:
    count = 0
    while box:
        count += 1
        for i in crane:
            if not box:
                break
            else:
                for j in range(len(box)):
                    if box[j] <= i:
                        box.pop(j)
                        break
    print(count)