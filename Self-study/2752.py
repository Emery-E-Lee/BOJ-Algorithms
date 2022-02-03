#오름차순으로 정리

A = list(map(int, input().split()))
A = sorted(A)

for i in range(len(A)):
  print(A[i], end = ' ')

'''
JS를 같이 공부하다보니
리스트의 길이를 자꾸 A.length로 한다
파이썬은 len(A)로 사용한다는 것을 기억하자

오름차순으로 정리하는 것은
메서드 sort()와 내장 함수 sorted()가 있다

sort()는 리스트 안에서 자리만 바꾸는 것이고,
sorted()는 정렬한 후 리스트를 새로 만든다

sort()는 리스트에서만 정의되고,
sorted()는 모든 이터러블에서 사용 가능하다

*사용 방법

A.sort()
sorted(A)


* 내림차순

A.sort(reverse=True)
sorted(A, reverse=True)
'''