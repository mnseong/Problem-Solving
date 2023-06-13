import sys
input = sys.stdin.readline

cnt = 0


def check(x, y, len):
    for i in range(x, x + len):
        for j in range(y, y + len):
            if tiles_map[i][j] != 0:
                return False
    return True


def divide(x, y, len):
    global cnt

    cnt += 1
    half = len // 2

    if check(x, y, half):
        tiles_map[x + half - 1][y + half - 1] = cnt
    if check(x, y + half, half):
        tiles_map[x + half - 1][y + half] = cnt
    if check(x + half, y, half):
        tiles_map[x + half][y + half - 1] = cnt
    if check(x + half, y + half, half):
        tiles_map[x + half][y + half] = cnt

    if len == 2:
        return

    divide(x, y, half)
    divide(x + half, y, half)
    divide(x, y + half, half)
    divide(x + half, y + half, half)


k = int(input())
x, y = map(int, input().split())
tiles_map = [[0] * (2 ** k + 1) for _ in range(2 ** k + 1)]
tiles_map[y - 1][x - 1] = -1

divide(0, 0, (1 << k))

for i in range((1 << k)-1, -1, -1):
    for j in range(1 << k):
        print(tiles_map[i][j], end=' ')
    print()
