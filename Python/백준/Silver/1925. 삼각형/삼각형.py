import sys
input = sys.stdin.readline
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
    print("X")
else:
    d1 = (x1 - x2)**2 + (y1 - y2)**2
    d2 = (x2 - x3)**2 + (y2 - y3)**2
    d3 = (x3 - x1)**2 + (y3 - y1)**2
    l = sorted([d1, d2, d3])
    if l[0] == l[1] == l[2]:
        print("JungTriangle")
    elif l[0] == l[1] or l[1] == l[2]:
        if l[0] + l[1] == l[2]:
            print("Jikkak2Triangle")
        elif l[0] + l[1] < l[2]:
            print("Dunkak2Triangle")
        else:
            print("Yeahkak2Triangle")
    else:
        if l[0] + l[1] == l[2]:
            print("JikkakTriangle")
        elif l[0] + l[1] < l[2]:
            print("DunkakTriangle")
        else:
            print("YeahkakTriangle")