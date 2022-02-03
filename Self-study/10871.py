import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range (0, N):
  if  A[i] < X:
    print(A[i], end = ' ') #끝에 공백

"""
참고. list 만들어 넣기
    

Smaller = []
 for i in range (0, N):   
    if A[i] < X:
        Smaller.append(A[i])
    
print(Smaller)


그런데 이렇게 리스트로 출력하면 틀린다고 나온다
또 for문을 써 줘서 출력해야하기 때문에
그냥 위에 올린 것처럼 바로 print하는 게 더 편하다

"""
