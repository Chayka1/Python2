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

def task_3_1():
    day = int(input('Введите число от 1 до 7: '))

    if day == 1:
        print('Понедельник')
    elif day == 2:
        print('Вторник')
    elif day == 3:
        print('Среда')
    elif day == 4:
        print('Четверг')
    elif day == 5:
        print('Пятница')
    elif day == 6:
        print('Суббота')
    elif day == 7:
        print('Воскресение')
    else:
        print('Ошибка, введите число в диапазоне от 1 до 7!')

def task_3_2():
    dlina_1 = float(input('Введите длину 1 прямоугольника: '))
    shirina_1 = float(input('Введите шиирину 1 прямоугольника: '))
    dlina_2 = float(input('Введите длину 2 прямоугольника: '))
    shirina_2 = float(input('Введите шиирину 2 прямоугольника: '))

    s_1 = dlina_1 * shirina_1
    s_2 = dlina_2 * shirina_2
    max = s_1

    if s_1 == s_2:
        print('Площади одинаковые')
    elif max < s_1:
        max = s_1
    elif max < s_2:
        max = s_2

    print(f'Максимальная площадь равна {max}')

def task_3_3():
    age = int(input('Введите возраст: '))

    if age > 0 and age <= 1:
        print('Вы младенец!')
    elif age > 1 and age < 13:
        print('Вы ребенок!')
    elif age >= 13 and age < 20:
        print('Вы подросток!')
    elif age >= 20:
        print('Вы взрослый!')
    else:
        print('Введите правильный возраст!')

def task_3_4():
    rom_number = int(input('Введите число от 1 до 10: '))

    if rom_number == 1:
        print('I')
    elif rom_number == 2:
        print('II')
    elif rom_number == 3:
        print('III')
    elif rom_number == 4:
        print('IV')
    elif rom_number == 5:
        print('V')
    elif rom_number == 6:
        print('VI')
    elif rom_number == 7:
        print('VII')
    elif rom_number == 8:
        print('VIII')
    elif rom_number == 9:
        print('IX')
    elif rom_number == 10:
        print('XX')
    else:
        print('Ошибка! Введите чилсо в дапазоне от 1 до 10!')


def task_3_5():
    waith = float(input('Введите массу тела: '))
    waith_n = waith * 9.8

    if waith_n > 500:
        print('Тело слишком тяжелое!')
    elif waith_n < 100:
        print('Тело слишком легкое!')

def task_3_6():
    mounth = int(input('Введите месяц: '))
    day = int(input('Введите день: '))
    year = int(input('Введите год: '))

    day_mounth = day * mounth

    if year == day_mounth:
        print('Это волшебная дата!')
    else:
        print('Это не волшебная дата!')

def task_3_7():
    color_1 = input('Введите первый цвет: ')
    color_2 = input('Введите второй цвет: ')

    if color_1 == 'красный' and color_2 == 'синий':
        print('Получиться фиолетовый!')
    elif color_1 == 'красный' and color_2 == 'желтый':
        print('Получиться оранжевый!')
    elif color_1 == 'синий' and color_2 == 'желтый':
        print('Получиться зеленый!')
    elif color_1 == 'синий' and color_2 == 'красный':
        print('Получиться фиолетовый!')
    elif color_1 == 'желтый' and color_2 == 'красный':
        print('Получиться оранжевый!')
    elif color_1 == 'желтый' and color_2 == 'синий':
        print('Получиться зеленый!')
    elif color_1 == 'красный' and color_2 == 'красный':
        print('Получиться красный!')
    elif color_1 == 'желтый' and color_2 == 'желтый':
        print('Получиться желтый!')
    elif color_1 == 'синий' and color_2 == 'синий':
        print('Получиться синий!')
    else:
        print('Ошибка! Введите правильный цвет!')

def task_3_8():
    people = int(input('Введите количество человек: '))
    hot_dogs = int(input('Введите количество хот-догов каждому участнику: '))
    count_hot_dogs = people * hot_dogs

    if count_hot_dogs % 10 != 0:
        min_package_sausages = count_hot_dogs // 10 + 1
        exstra_sasuges = min_package_sausages * 10 - count_hot_dogs
    else:
        min_package_sausages = count_hot_dogs // 10
        exstra_sasuges = 0
    if count_hot_dogs % 8 != 0:
        min_package_buns = count_hot_dogs // 8 + 1
        exstra_buns = min_package_buns * 8 - count_hot_dogs
    else:
        min_package_buns = count_hot_dogs // 8
        exstra_buns = 0
    print("Минимальное количество упаковок с сосисками: ", min_package_sausages)
    print("Количество оставшихся сосисок: ", exstra_sasuges)
    print("Минимальное количество упаковок с булочками: ", min_package_buns)
    print("Количество оставшихся булочек: ", exstra_buns)

def task_3_9():
    number = int(input('Введите число кармана: '))

    if number == 0:
        print('Этот карман зеленого цвета!')
    elif number >= 1 and number <= 10:
        if number % 2 == 0:
            print('Этот карман черного цвета!')
        else:
            print('Этот карман красного цвета!')
    elif number >= 11 and number <= 18:
        if number % 2 == 0:
            print('Этот карман красного цвета!')
        else:
            print('Этот карман черного цвета!')
    elif number >= 19 and number <= 28:
        if number % 2 == 0:
            print('Этот карман черного цвета!')
        else:
            print('Этот карман красного цвета!')
    elif number >= 29 and number <= 36:
        if number % 2 == 0:
            print('Этот карман красного цвета!')
        else:
            print('Этот карман черного цвета!')
    else:
        print('Ошибка! Введите число в диапазоне от 0 до 36!')

def task_3_10():
    five_cent = int(input('Введите количество 5 копеечных монет: '))
    ten_cent = int(input('Введите количество 10 копеечных монет: '))
    fifty_cent = int(input('Введите количество 50 копеечных монет: '))

    five_cent *= 5
    ten_cent *= 10
    fifty_cent *= 50
    total = five_cent + ten_cent + fifty_cent

    if total == 100:
        print('Поздравляем! Сумма всех копеек составил один рубль!')
    else:
        print('Введенная сумма не ровняется 1 рублю!')

def task_3_11():
    number_of_books = int(input('Введите количество приобретенных книг: '))

    if number_of_books == 0:
        print('Вы заработали 0 очков!')
    elif number_of_books == 2:
        print('Вы заработали 5 очков!')
    elif number_of_books == 4:
        print('Вы заработали 15 очков!')
    elif number_of_books == 6:
        print('Вы заработали 30 очков!')
    elif number_of_books == 8:
        print('Вы заработали 60 очков!')

def task_3_12():
    pockets = int(input('Введите количество приобретенных пакетов: '))
    one_pockets = 99
    total_sum = one_pockets * pockets

    if pockets > 0 and pockets < 10:
        print(f'Сумма скидки: 0% \nСумма покупки: {total_sum}')
    elif pockets >= 10 and pockets <= 19:
        sell = total_sum * 0.1
        total_sum -= sell
        print(f'Сумма скидки: {sell} \nСумма покупки: {total_sum}')
    elif pockets >= 20 and pockets <= 49:
        sell = total_sum * 0.2
        total_sum -= sell
        print(f'Сумма скидки: {sell} \nСумма покупки: {total_sum}')
    elif pockets >= 50 and pockets <= 99:
        sell = total_sum * 0.3
        total_sum -= sell
        print(f'Сумма скидки: {sell} \nСумма покупки: {total_sum}')
    elif pockets >= 100:
        sell = total_sum * 0.4
        total_sum -= sell
        print(f'Сумма скидки: {sell} \nСумма покупки: {total_sum}')
    else:
        print('Ошибка! Введите действитильное количество пакетов!')

def task_3_13():
    waith = float(input('Введите массу пакета: '))

    if waith <= 200:
        print('Сумма доставки 150 рублей!')
    elif waith > 200 and waith <= 600:
        print('Сумма доставки 300 рублей!')
    elif waith > 600 and waith <= 1000:
        print('Сумма доставки 400 рублей!')
    elif waith > 1000:
        print('Сумма доставки 475 рублей!')
    else:
        print('Ошибка! Введите правильную сумму!')

def task_3_14():
    waith = float(input('Введите ваш вес в килограмах: '))
    growth = float(input('Введите ваш рост в метрах: '))
    imt = waith / growth

    if imt >= 18.5 and imt <= 25:
        print('У вас оптимальнач масса тела!')
    elif imt < 18.5:
        print('Вы весите меньше оптимальной массы тела!')
    elif imt > 25:
        print('Вы весите больше оптимальной массы тела!')

def task_3_15():
    sec = int(input('Введите количество секунд: '))

    if sec > 0 and sec < 60:
        print(f'{sec} секунд')
    elif sec >= 60 and sec < 3600:
        min = sec // 60
        sec = sec - (min * 60)
        print(f'{min} минут, {sec} секунд')
    elif sec >= 3600 and sec < 86400:
        hour = sec // 3600
        min = (sec - 3600) // 60
        sec = sec - ((hour * 3600) + (min * 60))
        print(f'{hour} час ,{min} минут, {sec} секунд')
    elif sec >= 86400:
        day = sec // 86000
        hour = (sec - (day * 86000)) // 3600
        min = (sec - ((day * 86000) + (hour * 3600))) // 60
        sec = sec - ((day * 86000) + (hour * 3600) + (min * 60))
        print(f'{day} день ,{hour} час ,{min} минут, {sec} секунд')

def task_3_16():
    year = int(input('Введите год: '))

    if year % 100 == 0 and  year % 400 == 0:
        print('Этот год высокосный!')
    elif year % 4 == 0:
        print('Этот год высокосный!')
    else:
        print('Этот год не высокосный!')

def task_3_17():
    print('Перезагрузите компьютер и попробуйте подключиться')
    wifi = input('Испраили проблему: да/нет?\n')
    if wifi == 'нет':
        print('Перезагрузите маршрутизатор и попробуйте подключиться')
        wifi = input('Испраили проблему: да/нет?\n')
        if wifi == 'нет':
            print('Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены')
            wifi = input('Испраили проблему: да/нет?\n')
            if wifi == 'нет':
                print('Переместите маршрутизатор на новое место')
                wifi = input('Испраили проблему: да/нет?\n')
                if wifi == 'нет':
                    print('Возьмите новый маршрутизатор')
                else:
                    print('Приятного использования!')
            else:
                print('Приятного использования!')
        else:
            print('Приятного использования!')
    else:
        print('Приятного использования!')

def task_3_18():
    vegetarian = input('Будет ли на ужине вегетерианец?\n')
    vegan = input('Будет ли на ужине веганец?\n')
    gluten_free = input('Будет ли на ужине приверженец без глютеновой диеты?\n')
    if vegetarian == 'да':
        if vegan == 'да':
            if gluten_free == 'да':
                print('Вот ваши варианты ресторанов: \nКафе за углом\nКухня шеф-повара')
            else:
                print('Извините! Для вас нету вариатов ресторанов!')
        else:
            if gluten_free == 'да':
                print('Вот ваши варианты ресторанов: \nЦентральная пицерия')
            else:
                print('Вот ваши варианты ресторанов: \nБлюда от итальянской мамы')

    else:
        if vegan == 'да':
            if gluten_free == 'да':
                print('Извините! Для вас нету вариатов ресторанов!')
            else:
                print('Извините! Для вас нету вариатов ресторанов!')

        else:
            if gluten_free == 'да':
                print('Извините! Для вас нету вариатов ресторанов!')
            else:
                print('Вот ваши варианты ресторанов: \nИзысканные гамбургеры от Джо')

def task_2_1():
    product = 0
    number = int(input('Введите число: '))
    while product < 300:
        number *= 10
        product = number
        print(product)

def task_2_2():
    yes = 'да'
    while yes == 'да':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        print(f'{num1} + {num2} = {num1 + num2}')
        yes = input('Желаете выполнить операцию ещё раз? да/нет\n')

def task_2_3():
    for num in range(0, 1001, 10):
        print(num)

def task_2_4():
    num = int(input('Введите число: '))
    for num_ in range(num, num + 10):
        print(num_)

