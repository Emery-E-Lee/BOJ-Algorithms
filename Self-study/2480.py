a, b, c = map(int, input().split())

if a == b == c:
    print(int(10000 + (a * 1000)))
elif a != b and b != c and a != c:
    if a > b and a > c:
        big = a
    elif b > a and b > c:
        big = b
    else:
        big = c
    print(int(big*100))
else:
    if a == b:
        print(int(1000 + 100 * a))
    elif a == c:
        print(int(1000 + 100 * a))
    else:
        print(int(1000 + 100 * b))
    
