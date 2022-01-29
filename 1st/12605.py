import sys
input = sys.stdin.readline

N = int(input()) #문장 개수
for i in range(1, N+1):#1~N까지 loop
    words = list(input().strip().split())
    """
    입력된 문장(input)을 띄어쓰기 기준으로 자르고(split),
    양 옆 공백을 잘라(strip()) 리스트에 저장(list) 후, words에 대입
    참고: lstrip(), rstrip()은 각각 왼쪽 공백과, 오른쪽 공백을 자른다.
          ()안에 숫자 등을 넣으면 그에 해당하는 숫자, 문자를 제거한다.
    """
    words.reverse() #words의 순서를 거꾸로 뒤집기 / words[::-1]로도 가능하다.
    print('Case #%d: %s' %(i, " ".join(words))) 
    """
    'Case #숫자: words'형식을 만들기 위해, format()옵션 사용 / join()을 이용해 단어 사이에 공백을 넣어 하나로 만들어 준다. 
    참고: %d: 숫자(digit), %s: 문자열(string), %f: 실수(float)
    join 예시: ".".join(str) → 'welcome.to.my.home
    """
