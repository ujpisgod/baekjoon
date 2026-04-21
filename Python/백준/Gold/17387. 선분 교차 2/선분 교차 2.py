import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())
def ccw(ax,ay,bx,by,cx,cy):
    v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax)
    if v>0:
        return 1
    if v<0:
        return -1
    return 0

ab_c=ccw(x1,y1,x2,y2,x3,y3)
ab_d=ccw(x1,y1,x2,y2,x4,y4)
cd_a=ccw(x3,y3,x4,y4,x1,y1)
cd_b=ccw(x3,y3,x4,y4,x2,y2)

if ab_c*ab_d==0 and cd_a*cd_b==0:
    if (min(x1,x2),min(y1,y2))>(max(x3,x4),max(y3,y4)) or \
       (min(x3,x4),min(y3,y4))>(max(x1,x2),max(y1,y2)):
        print(0)
    else:
        print(1)
else:
    if ab_c*ab_d<=0 and cd_a*cd_b<=0:
        print(1)
    else:
        print(0)