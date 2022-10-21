'''
2020 KAKAO BLIND RECRUITMENT > "문자열 압축"
"https://programmers.co.kr/learn/courses/30/lessons/60057"
'''


def solution(s):
    ret = len(s) # 반환할 최소값

    # 문자열을 N/2 보다 크게 잘랐을 때는 압축 불가, 1 ~ N/2 범위에서 완전 탐색
    for i in range(1, len(s) // 2 + 1):
        segments = [s[j:j + i] for j in range(0, len(s), i)]  # s를 구간마다 slicing해서 list생성
        length = 0  # 각 단위 길이마다 계산된 압축된 문자열의 길이
        cnt = 1  # 반복되는 구간의 개수

        # list를 한 구간 씩 왼쪽으로 밀고, 원래 list와 같은 idx끼리 비교 -> 문자열이 반복되는지 확인
        for a, b in zip(segments, segments[1:] + ['']):
            if a == b:
                cnt += 1
            else:
                length += (len(str(cnt)) if cnt > 1 else 0) + len(a)
                cnt = 1
        ret = min(ret, length) # 반환값 갱신
    return ret