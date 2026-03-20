import sys
input=sys.stdin.readline
n=int(input())
n1=list(map(int,input().split()))
m=int(input())
m1=list(map(int,input().split()))
n1.sort()
def binary_search(target, data):
    start = 0
    end = len(data) - 1    
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True 
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False 
for i in m1:
    if binary_search(i, n1):
        print(1)
    else:
        print(0)
        