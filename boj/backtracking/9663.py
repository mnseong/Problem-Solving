"""
"N-Queen"
"https://www.acmicpc.net/problem/9663"
"""

import sys

input = sys.stdin.readline


def is_valid(n, board):
    for i in range(n):
        if board[n] == board[i] or n - i == abs(board[n] - board[i]):
            return False
    return True


def dfs(depth, board):
    global result

    if depth == N:
        result += 1

    for i in range(N):
        if not visited[i]:
            board[depth] = i

            if is_valid(depth, board):
                visited[i] = True
                dfs(depth+1, board)
                visited[i] = False


N = int(input())
visited = [False] * N
board = [0] * N
result = 0

dfs(0, board)
print(result)

