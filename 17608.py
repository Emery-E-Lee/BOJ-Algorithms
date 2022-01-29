import sys

n = int(sys.stdin.readline())
#막대기 개수

bars = [int(sys.stdin.readline()) for _ in range(n)]
# '_'는 값을 무시할 때 사용, index가 필요없는 for loop(ex.단순반복)를 작성할 때도 사용한다


tallist = bars.pop() #제일 긴 막대기, 맨 뒤의 막대를 제일 긴 막대기로 초기화/ 'pop()'은 리스트의 '맨 마지막' 요소를 돌려주고 그 요소를 삭제한다

cnt = 1 #보이는 막대기 수, 1로 초기화

for i in range(1, n):
  now = bars.pop() #현재 막대기 높이

  if now > tallist: 
    cnt += 1 #카운트
    tallist = now #가장 긴 막대기를 현재 막대기로 초기화

print(cnt) #보이는 막대기 수 출력
