# 생태학 https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin # 여러줄을 입력 받을 때
                  # sys.stdin은 ^Z를 입력받으면 종료, 개행문자(줄바꿈문자)까지 입력

Trees = {}  # Trees 딕셔너리 생성
tree_cnt = 0 # 나무 카운트 0으로 초기화

for line in input:
    if line == '\n':        # 개행문자만 입력됐을 경우 종료
        break

    tree = line.rstrip()
    tree_cnt += 1 # 나무 카운트 +1

    if tree in Trees:   
        Trees[tree] += 1    # 딕셔너리에 이미 있는 key면 value +1
    else:
        Trees[tree] = 1     # 딕셔너리에 없는 key면 key와 value=1 추가

Trees = sorted(Trees.items(), key = lambda x : x[0]) # key 값을 기준으로 정렬

# items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍(튜플 형태)을 얻을 수 있다
# 'lambda 매개변수: 표현식'


def tree_percent(a):
    percent = round((a / tree_cnt) * 100, 4) # round() 사용, 소수점 5번째 자리에서 반올림
    return percent

# def 함수이름(): - 첫 행
#          본문  - 함수를 호출했을 때 실행할 코드 블록


# 출력
for k, v in Trees: # 딕셔너리 Trees의 key와 value 값을 받아 출력
    percent = tree_percent(v)
    print(k, '%.4f' %percent) # 소수점 4자리까지 출력