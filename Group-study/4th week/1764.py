# 듣보잡 https://www.acmicpc.net/problem/1764
# 집합 사용

import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # N: 듣도 못한 사람, M: 보도 못한 사람

deud = []
for _ in range(0,N): # 듣도 못한 사람 명단 저장
    n = input().rstrip()
    deud.append(n)

bo = []
for _ in range(0,M): # 보도 못한 사람 명단 저장
    m = input().rstrip()
    bo.append(m)

deud_bo = set(deud).intersection(set(bo)) # 명단에 중복되는 이름이 없기때문에 집합 사용
                                          # intersection(교집합) 

print(len(deud_bo)) # 듣보잡 수 출력
for x in sorted(deud_bo): # 듣보잡 사전 순으로 출력
    print(x)