a=int(input())
b=" "
c="*"
for i in range(1,2*a):
    print(b*abs(a-i)+c*(2*(a-abs(a-i))-1))