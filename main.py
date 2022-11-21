def task_1_1(x):
    if x > 100:
        y = 20
        z = 40
    print(f'y = {y}, z = {z}')

def task_1_2(a):
    if a < 10:
        b = 0
        c = 1
    print(f'b = {b}, z = {c}')

def task_1_3(a):
    if a < 10:
        b = 0
    else:
        b = 99
    print(f'b = {b}')

def task_1_4():
    score = 0
    a_score = 0
    b_score = 0
    c_score = 0
    d_score = 0
    if score >= a_score:
        print('Ваш уровень - А.')
    else:
        if score >= b_score:
            print('Ваш уровень - В. ')
        else:
            if score >= c_score:
                print('Ваш уровень - С. ')
            else:
                if score >= d_score:
                    print('Baш уровень - D.')
                else:
                    print('Ваш уровень - F. ')

def task_1_5():
    amount1 = 11
    amount2 = 60
    max = amount1
    if amount1 > 10 and amount2 < 100:
        if max < amount1:
            max = amount1
        elif max < amount2:
            max = amount2
    print(f'Максимальное значение равно {max}')

def task_1_6(speed):
    if 24 < speed and speed < 56:
        print('Скорость нормальная!')
    else:
        print('Скорость аварийная!')

def task_1_7(points):
    if 9 < points and points < 51:
        print('Недопустимые точки!')
    else:
        print('Допустимые точки!')

def task_1_8():
    print('Error')

def task_1_9():
    print('Error')

def task_1_10():
    print('Error')
