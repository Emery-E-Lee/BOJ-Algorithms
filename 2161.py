n = int(input())
#n개의 카드
cards = [i for i in range(1, n+1)]
#1~n까지 배열을 만든다

while len(cards) > 1: #한 장이 남을 때까지 반복 
    print(cards.pop(0), end = ' ')
    #cards[0]의 숫자 출력 & 삭제, 숫자 뒤에 공백 출력
    last = cards.pop(0)
    #두번째 카드를 뽑아낸다 / 첫번째 카드는 버렸으므로, 다시 cards[0]을 뽑는다 
    cards.append(last)
    #맨 뒤에, 뽑아낸 두번째 장을 넣는다

print(cards[0])
#마지막 남은 한 장을 출력