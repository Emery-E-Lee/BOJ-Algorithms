#런타임 에러가 난다..

import sys

N , M = map(int, sys.stdin.readline().split())

N_cd = [int(sys.stdin.readline().strip()) for _ in range(N)]
M_cd = [int(sys.stdin.readline().strip()) for _ in range(M)]

while True:
    a, b = map(int, sys.stdin.readline().split()) #입력을 받는다.
    if a == 0 and b == 0:  #맨 마지막에 0 0이 입력되면 루프 종료
        break

cnt = 0

i = 0
j = 0

while True:
    if (i == N) or (j == M):
        break
    if (N_cd[i] < M_cd[j]):
        i += 1
    elif (N_cd[i] > M_cd[j]):
        j += 1
    else:
        i += 1
        j += 1
        cnt += 1


print(cnt)