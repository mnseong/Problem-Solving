# 문자열 재정렬

s = input()

alphabets = [x for x in s if x.isalpha() == True]
numbers = [int(n) for n in s if n.isdigit() == True]

alphabets.sort()
alphabets.append(str(sum(numbers)))
result = ''.join(alphabets)

print(result)