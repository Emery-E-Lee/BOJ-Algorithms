# 스택 - https://www.acmicpc.net/problem/10828

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

N = int(input()) # 명령의 수 입력

stack = [] # 스택 리스트 생성

for _ in range(0,N):
    word = input().split() # ex) push 1 (각각 word[0], word[1])
    order = word[0] # '명령'을 order에 대입

    if order == 'push':
        stack.append(int(word[1])) # 스택에 넣기

    elif order == 'pop':
        if len(stack) == 0: # 스택에 정수가 없는 경우
            print(-1) # -1 출력
        else:
            print(stack.pop()) # 가장 위 정수를 빼내어 출력
    
    elif order == 'size': 
        print(len(stack)) # 스택의 정수 개수 출력

    elif order == 'empty':
        if len(stack) == 0: #스택이 비어있으면
            print(1) # 1 출력
        else: # 스택이 차 있으면
            print(0) # 0 출력

    elif order == 'top':
        if len(stack) == 0: # 스택이 비어있으면
                print(-1) # -1 출력
        else: # 스택이 차 있으면
            print(stack[-1]) # 스택 가장 위 정수(리스트 가장 끝) 출력