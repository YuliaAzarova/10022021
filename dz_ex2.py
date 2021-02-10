n = 7
for i in range(n):
    for j in range(n):
        if i + j == 1 or i + j == (n - 1) + (n - 2):
            print('.',end=' ')
        elif i + j == n - 2 or i + j == n:
            print('.',end=' ')
        elif i + j == n - 4 or i + j == n:
            print('.',end=' ')
        elif i + j == n + 2 or i + j == n:
            print('.',end=' ')
        else:
            print('*', end = ' ')
    print()