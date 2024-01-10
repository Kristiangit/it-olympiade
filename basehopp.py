N, tårn = map(int, input().split())

bakke = [int(x) for x in input().split()]

for _ in range(tårn):

    x, y = map(int, input().split())
    fin1, fin2 = False, False

    
    for i in range(y):
        i = -i -1
        if (not fin1):
            if x+i < 0: 
                fin1 = True
            elif bakke[x+(i)] > y+(i):
                fin1 = True
        i = -i
        if (not fin2):
            if x+i >= N:
                fin2 = True
            elif bakke[x+(i)] > y-(i):
                fin2 = True
                ...

        if fin1 and fin2:
            i -= 1
            break

    print(i)


"""
10 2
3 1 1 2 3 4 2 2 1 1
1 5
4 5
"""