'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기) > "로또의 최고 순위와 최저 순위"
"https://programmers.co.kr/learn/courses/30/lessons/77484"
'''


def solution(lottos, win_nums):
    same = len([n for n in lottos if n in win_nums])  # 민우의 복권 번호 중 당첨 번호와 같은 것의 개수
    zero = lottos.count(0)  # 민우의 복권 중 알아볼 수 없는 번호의 개수
    return [7 - max(same + zero, 1), 7 - max(same, 1)]