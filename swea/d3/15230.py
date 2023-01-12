# 삼성 SW Expert Academy - 15230. 알파벳 공부

n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(1, n + 1):
    s = input()
    cnt = 0
    for j in range(len(s)):
        if s[j] == alphabet[j]:
            cnt += 1
        else:
            break;
    print("#{0} {1}".format(i, cnt))
    
# 삼성 SWEA의 경우 output format 주의할 것...