# 자료구조는 정말 최고야 https://www.acmicpc.net/problem/23253
# 한 더미라도 내림차순이 아니면, 번호순 나열 불가능

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 교과서 수, M: 더미 수
p = True

for _ in range(M):
    i = int(input()) #: 더미 권수
    k = list(map(int, input().split())) # 더미 번호

    for j in range(i-1):  # 더미에 있는 번호가 내림차순인지 확인(아래부터 위로)
        if k[j] < k[j+1]: # 오름차순이면, p = false
            p = False
            break

print('Yes' if p else 'No') # p가 True면 Yes, False면 No