'''
Heap - 이중우선순위큐
"https://programmers.co.kr/learn/courses/30/lessons/42628"
'''

def solution(operations):
    answer = []
    for operation in operations:
        cmd, num = operation.split(' ')
        if cmd == 'I':
            answer.append(int(num))
        else:
            if not answer:
                continue
            if num == '1':
                answer.sort()
            else:
                answer.sort(reverse=True)
            answer.pop()
    answer.sort()
        
    return [0, 0] if not answer else [answer[-1], answer[0]]