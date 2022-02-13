# https://www.acmicpc.net/problem/5568
# permutation 이용

import sys
from itertools import permutations # 순열(순서 상관 X)을 쉽게 만들어주는 permutation 이용

input = sys.stdin.readline

all = int(input()) # 전체 카드 개수
pick = int(input()) # 뽑을 카드 개수

cards_list = [int(input()) for _ in range(all)]

result = set() # 집합 생성, 집합 특징: 중복을 허용하지 않는다.


for i in permutations(cards_list, pick): #cards_list에서 pick의 개수를 뽑아 만든 리스트 길이 만큼 for문이 돈다.
        result.add(''.join(map(str,i))) #join으로 뽑아낸 카드를 이어주고, set의 메서드 add 사용, 값을 추가. + TypeError가 나서 str으로 바꿔줌.
print(len(result))


""" 
permutation
for문을 이용하지 않고 순열을 구할 수 있다.

from itertools import permutations
a = [1,2,3]
permute = permutations(a,2)
print(list(permute))


결과
[(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]


import intertools
pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool))))  3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))  2개의 원소로 수열 만들기 """


"""
set: 수학의 집합과 같음
특징: 중복을 허용하지 않음. 순서가 없다. 즉, 인덱싱으로 값을 얻을 수 없다. 
중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.
인덱싱으로 접근하려면 '리스트'나 '튜플'로 변환 후 해야한다. """

