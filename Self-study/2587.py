import sys
num = [int(sys.stdin.readline().strip()) for _ in range(0,5)] #5개까지 입력

num.sort() #오름차순으로 정렬

avg = 0

for i in range (0,len(num)):
    avg += num[i]
print(int(avg/len(num)), end='\n') #int로 안 바꿔주면 '.0'이 같이 출력됨
print(num[2])