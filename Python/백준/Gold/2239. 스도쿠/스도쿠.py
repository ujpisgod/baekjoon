sdoku=[list(map(int,input().rstrip())) for i in range(9)]
tsdoku=[[] for i in range(9)]
coord=[]
squ=[[] for i in range(9)]
def sd(i,j):
    if i<3 and j<3:
        return 1
    elif i<3 and 3<=j<6:
        return 2
    elif i<3 and 6<=j<9:
        return 3
    elif 3<=i<6 and j<3:
        return 4
    elif 3<=i<6 and 3<=j<6:
        return 5
    elif 3<=i<6 and 6<=j<9:
        return 6
    elif 6<=i<9 and j<3:
        return 7
    elif 6<=i<9 and 3<=j<6:
        return 8
    elif 6<=i<9 and 6<=j<9:
        return 9
for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            coord.append((i,j,sd(i,j)))
for i in range(9):
    for j in range(9):
        tsdoku[i].append(sdoku[j][i])
for i in range(9):
    for j in range(9):
        squ[sd(i,j)-1].append(sdoku[i][j])
def solve(x):
    if x==len(coord):
        for i in sdoku:
            print(''.join(map(str,i)))
        exit()
    for num in range(1,10):
        if num not in sdoku[coord[x][0]] and num not in tsdoku[coord[x][1]] and num not in squ[coord[x][2]-1]:
            sdoku[coord[x][0]][coord[x][1]]=num
            tsdoku[coord[x][1]][coord[x][0]]=num
            squ[coord[x][2]-1].append(num)
            solve(x+1)
            sdoku[coord[x][0]][coord[x][1]]=0
            tsdoku[coord[x][1]][coord[x][0]]=0
            squ[coord[x][2]-1].pop()
solve(0)