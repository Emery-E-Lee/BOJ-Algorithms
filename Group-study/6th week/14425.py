# 문자열 집합 https://www.acmicpc.net/problem/14425
# set 이용, 중복 배제

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 문자열 개수 N, M 출력 

S = set() # Set 생성
count = 0

for _ in range(N): # 집합 S에 포함되어 있는 문자열 입력 받기
    Str = input().rstrip()
    S.add(Str) # 집합 S에 추가

for _ in range(M): # 검사해야하는 문자열 입력 받기
    Str = input().rstrip()
    
    if Str in S: # 입력 받은 문자열이 집합 S에 있으면,
        count += 1 # count +1

print(count) # count 출력
