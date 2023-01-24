'''
"회의실 배정"
"https://www.acmicpc.net/problem/1931"
'''


n = int(input())

times = []
result = 0
temp = 0
for _ in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

times = sorted(times, key = lambda x: x[0])
times = sorted(times, key = lambda x: x[1])

for i in range(n):
    if times[i][0] >= temp:
        result += 1
        temp = times[i][1]

print(result)