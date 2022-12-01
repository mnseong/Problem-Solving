'''
2019 KAKAO BLIND RECRUITMENT > "무지의 먹방 라이브"
"https://programmers.co.kr/learn/courses/30/lessons/42891"
'''

import heapq


def solution(food_times, k):
    # 방송이 중단된 시간에 남은 음식이 없는 경우
    if sum(food_times) <= k:
        return -1
    pq = []  # priority queue(힙을 이용한)
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i + 1))

    total = 0  # 남은 음식 수 * 해당 음식 먹는데 걸리는 시간
    prev = 0
    remain = len(food_times)
    while ((pq[0][0] - prev) * remain) <= k - total:
        now = heapq.heappop(pq)[0]
        total += (now - prev) * remain
        remain -= 1
        prev = now
    pq.sort(key=lambda x: x[1])  # 음식 번호를 기준으로 정렬

    return pq[(k - total) % len(pq)][1]