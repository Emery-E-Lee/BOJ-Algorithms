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

while True: # CD번호가 오름차순으로 정렬되어 있으므로, 인덱스 값을 이용
    # 두 리스트의 인덱스 0부터 비교, 요소 값이 작은 리스트의 인덱스를 +1 해서 비교한다
    if (N_cd[i] < M_cd[j]): 
        i += 1
    elif (N_cd[i] > M_cd[j]):
        j += 1
    else: # 요소 값이 같다면 count를 +1하고, 둘 다 다음 인덱스로 넘어가 비교
        i += 1
        j += 1
        cnt += 1
    if (i == N) or (j == M): # 둘 중 하나라도 갖고 있는 CD수에 다다르면, 종료
        break

print(cnt)