#친구가 '잉'을 마치 별찍기 문제처럼 보냈길래 만들어 봤다

n = int(input())


for i in range(1,n+1): #1~n까지 세로 길이 
  for j in range(n+1-i): #가로로 '잉'을 몇 개 찍을지
    print('잉', end='')  # '잉' 출력, end에 ''를 지정하여 줄바꿈을 하지 않는다
  print() # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
          # (print는 출력 후 기본적으로 다음 줄로 넘어감)

for i in range(2, n+1): #2~n까지 세로 길이, '잉'을 2개부터 찍기 때문에 2로 시작
  for j in range(i): 
    print('잉', end='')
  print()