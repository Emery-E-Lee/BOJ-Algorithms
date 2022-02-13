""" 두 점을 연결해서 x축과 y축에 평행한 직선이 되려면,
x좌표가 같거나, y좌표가 같은 상태에서 나머지 값이 달라야 한다. 
dictionary, defaultdict 이용
"""

import sys
from collections import defaultdict

input = sys.stdin.readline()

N = int(input)

x = defaultdict(list)
y = defaultdict(list)
result = 0

for _ in range(N):
    a, b = map(int, input().split())
    x[a].append(b)
    y[b].append(a)

for key in x:
    if len(x) >=2:
        result +=1

for key in y:
    if len(y) >=2:
        result +=1

print(result)

