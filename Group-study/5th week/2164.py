# 카드2 - https://www.acmicpc.net/problem/2164

# 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, 
# N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.(deque 사용)
# 우선, 제일 위에 있는 카드를 바닥에 버린다.(popleft)
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.(popleft > append)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 카드 장 수 입력

Deque = deque() # 덱 생성

for i in range(1, N+1): # 1~N까지 덱에 카드 순서대로 넣기 
    Deque.append(i)

while len(Deque) != 1: # 마지막 한장이 남을때 까지 반복
    Deque.popleft() # 제일 위의 카드 버리기
    temp = Deque.popleft() # 제일 위의 카드를 뽑아 temp에 담기
    Deque.append(temp) # temp에 담긴 카드를 제일 아래의 카드 밑으로 옮기기

print(Deque[0]) # 마지막 남은 카드를 출력