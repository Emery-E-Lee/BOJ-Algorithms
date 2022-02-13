from collections import deque

N, K = map(int, input().split())

que = deque()

for i in range(N): # i는 0부터 N-1
    que.append(i+1) #큐에 1~N까지 넣기

out = [] #제거된 사람 리스트

while len(que) != 0: #큐의 길이가 0이 되기 전까지 반복
    que.rotate(-(K-1)) #deque의 rotate를 이용, K번째 수가 맨 왼쪽으로 오도록 한다
    out.append(str(que.popleft())) #맨 왼쪽의 수를 뽑아내고 que에서 삭제한 후, out에 대입

print("<"+", ".join(out)+">")

# 참고: join은 str 함수이다
#.join(li_name) 
# ['a', 'b', 'c'] 를 'abc'의 문자열로 합쳐서 반환, 구분자가 공백이기 때문
#'_'.join(li_name)
# a_b_c 와 같은 문자열로 반환된다
