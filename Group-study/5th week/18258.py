# 큐2 - https://www.acmicpc.net/problem/18258

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys

input = sys.stdin.readline

N = int(input()) #명령의 수 입력

queue = deque() # 덱 생성

for _ in range(0,N):
    word = input().split() # 명령어, 숫자 입력
    order = word[0] # word[0] order에 대입

    if order == 'push':
        queue.append(int(word[1])) # 큐에 넣기

    elif order == 'pop':
        if len(queue) == 0: # 큐가 비어있을 경우
            print(-1) # -1 출력
        else: # 큐가 차 있을 경우
            print(queue[0]) # 큐에서 가장 앞에 있는 정수 출력
            queue.popleft() # 그 정수를 제거
    
    elif order == 'size':
        print(len(queue)) # 큐에 들어있는 정수 개수 출력

    elif order == 'empty': 
        if len(queue) == 0: # 큐가 비어있을 경우
            print(1) # 1 출력
        else: # 큐가 차 있을 경우 
            print(0) # 0 출력

    elif order == 'front':
        if len(queue) == 0: # 큐가 비어있을 경우 
            print(-1) # -1 출력
        else: # 큐가 차있을 경우
            print(queue[0]) # 가장 앞에 있는 정수 출력

    elif order == 'back':
        if len(queue) == 0: # 큐가 비어있을 경우
            print(-1) # -1 출력
        else: # 큐가 차있을 경우
            print(queue[-1]) # 가장 뒤에 있는 정수 출력
