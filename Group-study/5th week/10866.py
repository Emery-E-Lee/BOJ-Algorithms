# 덱 - https://www.acmicpc.net/problem/10866


# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque 
import sys
input = sys.stdin.readline

N = int(input()) # 명령의 수 입력

Deque = deque() # 덱 생성

for _ in range(0,N):
    order = input().split() # 명령어, 숫자 입력

    if order[0] == 'push_front':
        Deque.appendleft(int(order[1])) # 덱 앞에 정수 추가

    elif order[0] == 'push_back':
        Deque.append(int(order[1])) # 덱 뒤에 정수 추가

    elif order[0] == 'pop_front':
        if len(Deque) != 0: # 덱이 차 있을 경우
            print(Deque.popleft()) # 덱 앞에서 정수 빼기
        else: # 덱이 비어있을 경우
            print(-1) # -1 출력

    elif order[0] == 'pop_back': 
        if len(Deque) != 0: # 덱이 차 있을 경우
                print(Deque.pop()) # 덱 뒤에서 정수 빼기
        else: # 덱이 비어있을 경우
            print(-1) # -1 출력

    elif order[0] == 'size':
        print(len(Deque)) # 덱의 길이(정수 개수) 출력

    elif order[0] == 'empty':
        if len(Deque) == 0: #덱이 비어있으면
            print(1) # 1 출력
        else: #덱이 차 있으면
            print(0) # 0 출력
    
    elif order[0] == 'front':
        if len(Deque) == 0: #덱이 비어있으면
            print(-1) # -1 출력
        else: #덱이 차 있으면
            print(Deque[0]) # 덱 가장 앞에 있는 정수 출력

    elif order[0] == 'back':
        if len(Deque) == 0: #덱이 비어있으면
            print(-1) # -1 출력
        else: #덱이 차 있으면
            print(Deque[-1]) # 덱 가장 뒤에 있는 정수 출력
