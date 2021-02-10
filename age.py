ima = input('Как тебя зовут?\n')
age = int(input('Сколько тебе лет?\n'))
if age < 2 or age == 2:
    n = 7
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1 or j == n // 2 or i == n // 2:
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()
    print('Ты - младенец')
elif age > 2 and age < 7 or age == 7:
    n = 7
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('.', end=' ')
            else:
                print('*', end=' ')
        print()
    print('Ты - дошкольник')
elif age > 7 and age < 12 or age == 12:
    n = 5
    for i in range(n-1):
        for j in range(n):
            if i == 0 and j == 2:
                print('*', end = ' ')
            elif i == 1 and j == 1:
                print('*', end=' ')
            elif i == 1 and j == 2:
                print('*', end=' ')
            elif i == 1 and j == 3:
                print('*', end=' ')
            elif i == 2 and j == 0:
                print('*', end = ' ')
            elif i == 2 and j == 1:
                print('*', end=' ')
            elif i == 2 and j == 2:
                print('*', end=' ')
            elif i == 2 and j == 3:
                print('*', end = ' ')
            elif i == 2 and j == 4:
                print('*', end = ' ')
        print()