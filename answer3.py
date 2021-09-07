def recur(n, cur):
    if (cur == False):
        cur = 0
    if (n < 2):
        print('Invalid input')
    else:
        for x in range(cur, 1, -1):
            a = n
            n = n - 1
            cur = cur + 1 / (a * (a - 1))
        print( 1 / n + cur)
recur(3,True)
recur(6,False)
recur(1,True)
