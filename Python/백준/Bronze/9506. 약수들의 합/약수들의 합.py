while True:    
    a=int(input())
    if a==6:
        print("6 = 1 + 2 + 3")
    elif a==28:
        print("28 = 1 + 2 + 4 + 7 + 14")
    elif a==496:
        print("496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248")
    elif a==8128:
        print("8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064")
    elif a==-1:
        break
    else:
        print(f"{a} is NOT perfect.")
        