'''
"롤러코스터"
"https://www.acmicpc.net/problem/2873"
'''


import sys

input = sys.stdin.readline

row, column = map(int, input().rstrip().split())
plot = [list(map(int, input().rstrip().split())) for _ in range(row)]

direction = ['U', 'R', 'L', 'D']

if row % 2 == 1:
    for _ in range(row//2):
        print(direction[1]*(column-1), end = '')
        print(direction[3], end = '')
        print(direction[2]*(column-1), end = '')
        print(direction[3], end = '')
    print(direction[1]*(column-1))
elif column % 2 == 1:
    for _ in range(column//2):
        print(direction[3]*(row-1), end = '')
        print(direction[1], end = '')
        print(direction[0]*(row-1), end = '')
        print(direction[1], end = '')
    print(direction[3]*(row-1))
elif column % 2 == 0 and row % 2 == 0:
    minValue = 1000
    spot = [-1, -1]
    for i in range(row):
        if i % 2 == 0:
            for j in range(1, column, 2):
                if minValue > plot[i][j]:
                    spot = [i, j]
                minValue = min(minValue, plot[i][j])
        else:
            for j in range(0, column, 2):
                if minValue > plot[i][j]:
                    spot = [i, j]
                minValue = min(minValue, plot[i][j])
            
    result = (direction[3]*(row-1) + direction[1] + direction[0]*(row-1) + direction[1])*(spot[1]//2)
    currentX = 2*(spot[1]//2)
    currentY = 0
    xBound = 2*(spot[1]//2) + 1
    while currentX != xBound or currentY != row-1:
        if currentX < xBound and [currentY, xBound] != spot:
            currentX += 1
            result += direction[1]
        elif currentX == xBound and [currentY, xBound-1] != spot:
            currentX -= 1
            result += direction[2]
        if currentY != row-1:
            currentY += 1
            result += direction[3]

    result += (direction[1] + direction[0]*(row-1) + direction[1] + direction[3]*(row-1))*((column-spot[1]-1)//2)
    print(result)