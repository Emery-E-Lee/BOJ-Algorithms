import sys
N = int(sys.stdin.readline()) # 출입 기록 수 N 입력
result = {} # 빈 딕셔너리 생성
for _ in range(N): # N번 만큼 반복
    name, status = map(str, sys.stdin.readline().split()) #값을 받아 스트링으로 변환, name, status에 대입
    if status == 'enter': #status가 'enter'라면,
        result[name] = True #'enter'가 주어진 사람의 이름을 dict의 key로 둔다
    else: #'leave'가 들어오면,
        del result[name] # 해당 이름인 사람을 dict에서 지운다
print("\n".join(sorted(result.keys(), reverse=True))) #dict의 모든 key를 가져와서 역순으로 정렬해서 출력한다