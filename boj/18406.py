'''
"럭키 스트레이트"
"https://www.acmicpc.net/problem/18406"
'''

n = input()
size = len(n)

a = sum([int(n[i]) for i in range(0, size // 2)])
b = sum([int(n[i]) for i in range(size // 2, size)])

if a == b:
    print("LUCKY")
else:
    print("READY")