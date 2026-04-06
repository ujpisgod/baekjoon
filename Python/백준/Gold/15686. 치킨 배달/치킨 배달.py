n, p = map(int, input().split())
m = [list(map(int, input().split())) for i in range(n)]

c = []
h = []

# 집과 치킨집 좌표 싹 모으기
for i in range(n):
    for j in range(n):
        if m[i][j] == 2:
            c.append((i, j))
        if m[i][j] == 1:
            h.append((i, j))
ll = []
def start(c_c):
    total_city_distance = 0
    for house in h:
        min_dist = float('inf') 
        for chic in c_c:
            dist = abs(house[0] - chic[0]) + abs(house[1] - chic[1])
            min_dist = min(min_dist, dist)
        total_city_distance += min_dist     
    ll.append(total_city_distance)
def getclist(start_idx, k):
    if len(c_c) == k:
        start(c_c)
        return
    for i in range(start_idx, len(c)):
        c_c.append(c[i])
        getclist(i + 1, k)
        c_c.pop()
c_c = []
getclist(0, p)
print(min(ll))