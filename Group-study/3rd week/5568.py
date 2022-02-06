# permutation을 이용

import sys
from itertools import permutations

input = sys.stdin.readline

all = int(input())
pick = int(input())

cards_list = [int(input()) for _ in range(all)]

result = set()

for i in permutations(cards_list, pick): #cards_list에서 pick의 개수를 뽑아 만든 리스트 길이 만큼 for문이 돈다.
        result.add(''.join(map(str,i))) #TypeError가 나서 str으로 바꿔줌

print(len(result))

# permutation
# for문을 이용하지 않고 순열을 구할 수 있다.
# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool))))  3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2))))  2개의 원소로 수열 만들기


#set: 수학의 집합과 같음, 특징:중복을 허용하지 않음. 순서가 없다. == 인덱싱으로 값을 얻을 수 없다. 
# 인덱싱으로 접근하려면 '리스트'나 '튜플'로 변환 후 해야한다.

