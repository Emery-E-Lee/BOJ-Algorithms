import sys
lst = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
work = dict() #dictionary 생성

for i in lst: # list 값을 하나씩 꺼내 pattern으로 전달
    work[i] = 0 # work의 value 값을 0으로 초기화 
    # {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}

count = 0
lines = sys.stdin.readline()
