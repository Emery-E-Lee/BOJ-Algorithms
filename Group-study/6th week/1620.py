# 나는야 포켓몬 마스터 이다솜 https://www.acmicpc.net/problem/1620
# 딕셔너리 사용, .isdigit() 사용 숫자 판별

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #'포켓몬 개수 N, 문제 개수 M' 입력받기

pokemon_name = {} # {포켓몬이름 : 포켓몬넘버} 딕셔너리 생성
pokemon_num = {}  # {포켓몬넘버 : 포켓몬이름} 딕셔너리 생성

for i in range(1, N+1): # 포켓몬 개수만큼 반복
    name = input().rstrip()
    pokemon_num[i] = name # {1: name1 , 2: name2 ...}
    pokemon_name[name] = i # {name1: 1, name2: 2 ...}

for _ in range(0,M): # 문제 개수만큼 반복
    q = input().rstrip()

    if q.isdigit(): # 숫자인지 판별
        print(pokemon_num[int(q)]) # q가 숫자면, pokemon_num에서 q를 찾아 해당 값을 출력
    else:
        print(pokemon_name[q]) # q가 숫자가 아닐 경우, pokemon_name에서 q를 찾아 해당 값을 출력