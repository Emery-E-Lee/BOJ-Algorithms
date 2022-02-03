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

"""
