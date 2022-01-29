import sys
n = int(sys.stdin.readline())
ticket = map(int, input().split()) #티켓 번호 입력 받기

ticket = sorted(ticket) #오름차순으로 정렬
c = 1 #가장 작은 값 1

for i in range(0, n): 
  if( c == ticket[i]): #ticket에 없는 번호 중 가장 작은 값을 찾아야 하므로, 이미 있는 번호인지 확인(ex.1과 ticket[0]이 같은지 확인) 후,
    c += 1 #있으면, 다음 번호를 비교를 위해 c에 +1을 해줌
  
print(c)
