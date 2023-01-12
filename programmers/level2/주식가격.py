'''
스택/큐 > 주식가격
"https://school.programmers.co.kr/learn/courses/30/lessons/42584#"
'''

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break;
            elif prices[i] <= prices[j]:
                answer[i] += 1
    return answer

'''
스택이나 큐를 사용하지 않은 풀이
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
'''