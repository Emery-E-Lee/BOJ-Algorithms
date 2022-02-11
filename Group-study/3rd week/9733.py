# 참고

import sys
lst = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
work = dict() #dictionary 생성

for i in lst: # list 값을 하나씩 꺼내 pattern으로 전달
    work[i] = 0 # work의 value 값을 0으로 초기화 
    # {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}

count = 0 # Total값 0으로 초기화
bees = list(sys.stdin.readline().split())

for i in bees: # bees에 있는 요소를 하나 씩 불러온다
    if i in lst: # bees에 있는 요소가 lst에 있다면,
        work[i] = work.get(i,0) + 1 # work의 key 값이 없을 때 0을 돌려주고, key 값이 있을 때는 value 값에 1을 더해준다.
        count +=1 # 카운트로 Total을 세어준다

for i in work: # work의 요소 print. i는 work의 key값, work.get(i)는 work의 value값
    print(i, work.get(i), '{:.2f}'.format(work.get(i)/count)) # 문자열 formatting, "{:.2f}".format(출력내용)

print('Total', count, '1.00')