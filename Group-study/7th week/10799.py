# https://www.acmicpc.net/problem/10799 쇠막대기

# '(' (막대 시작점)의 수를 세서 막대기의 수를 세고,
# 레이저 '()'가 들어오면, 그전까지의 막대기 수를 전부 전체 막대기 수에 다시 더해준다.
# ')'가 들어오면, 제일 마지막에 들어온 막대 시작점을 빼준다.
# 막대 시작점을 모은 스택의 길이를 재서 답을 구한다.


# '()'를 '*'문자열로 바꾸기
# 입력: ()(((()())(())()))(())
#       *(((**)(*)*))(*)
string = str(input()).replace('()','*')
string = list(string)   

def solution(arrangement):
    
    # answer = 쇠막대기 수
    answer = 0
    
    #stack리스트 만들기
    stick_stack = []


    for value in string:
        #만약 value가 (이면 , 쇠막대기 시작이므로
        if value == '(' :
            
            # 쇠막대기 수를 증가
            answer += 1
            
            #value를 스택에 추가 => 막대기 시작점 하나 '('를 추가
            stick_stack.append(value)
        
        #만약 막대기의 끝이면, 스택리스트에 pop() => 즉 제일 나중에 들어온 '('를 제거.
        elif value == ')' : stick_stack.pop()
        
        #레이저를 만나면 레이저가 자르려는 스택의 길이만큼 전체 길이에 다시 더해준다
        #쇠막대기 1개를 1번자르면 2개, 쇠막대기 2개를 1번자르면 4개식으로 늘어나기 때문
        else : answer += len(stick_stack)
    return answer

print(solution(string))