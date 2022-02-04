import sys
num = [int(sys.stdin.readline().strip()) for _ in range(0,5)]

num.sort()

avg = 0

for i in range (0,5):
    avg += num[i]
print(int(avg/len(num)), end='\n')
print(num[2])



