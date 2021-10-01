flag = True
while flag:
    try:
        a = int(input('Введите целочисленное значение a: \n'))
    except ValueError:
        print('Ошибка.')
    else:
        if (a >= 10000) and (a <= 99999):
            flag = False
        else:
            print('Число a должно быть пятизначным!')
r = 10
c = ''
i = 0
while i < 5:
    b = a % r;
    c = str((r - 1 - b)) + c;
    a = a // r;
    i += 1
print("a =", c)
