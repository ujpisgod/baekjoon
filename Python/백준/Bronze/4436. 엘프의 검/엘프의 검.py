
while True:
    try:
        n = int(input())
    except EOFError:
        break
    k = 1
    a = set()  
    while True:
        a.update(str(n * k)) 
        if len(a) == 10:      
            print(k)
            break
        k += 1