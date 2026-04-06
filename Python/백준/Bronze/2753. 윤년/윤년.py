a= int(input())

if (0 == a%4 and 0 != a%100) or 0 == a%400:
    print(1)
else:
    print(0)