import sys
from main import *

while True:
    print('1. Алгоритмичный тренажер №1\n' + '2. Алгоритмичный тренажер №2\n' + '3. Задачи по програмированию №1\n' + '4. Задачи по програмированию №2\n' + '0.Выход из меню')
    exercise = input()

    if exercise == '1':
        while True:
            print('1. Напишите инструкцию if, которая присваивает значение 20 переменной у и значение 40 переменной z, если переменная х больше 100.\n' +
                  '2. Напишите инструкцию if, которая присваивает значение О переменной b и значение 1 переменной с, если переменная а меньше 1О.\n' +
                  '3. Напишите инструкцию if-else, которая присваивает значение О переменной b, если переменная а меньше 1О. В противном случае она должна присвоить переменной b значение 99.\n' +
                  '4. Приведенный ниже фрагмент кода содержит несколько вложенных инструкций if-else. К сожалению, они были написаны без надлежащего выравнивания и выделения отступом. \n'
                  'Перепишите этот фрагмент и примените соответствующие правила выравнивания и выделения отступом.\n' +
                  '5. Напишите вложенные структуры принятия решения, которые выполняют следующее: если amountl больше 10 и amount2 меньше 100, то показать большее значение из двух переменных amountl и amount2.\n' +
                  '6. Напишите инструкцию if-else, которая выводит сообщение \'Скорость нормальная\', если переменная speed находится в диапазоне от 24 до 56. \n'
                  'Если значение переменной speed лежит вне этого диапазона, то показать \'Скорость аварийная\'.\n' +
                  '7. Напишите инструкцию if-else, которая определяет, находится ли переменная points вне диапазона от 9 до 51. Если значение переменной лежит вне этого диапазона, \n'
                  'то она должна вывести сообщение \'Недопустимые точки\' . В противном случае она должна показать сообщение \'Допустимые точки\' .\n' +
                  '8. Напишите инструкцию if, которая применяет библиотеку черепашьей графики, чтобы определить, находится ли угловое направление черепахи в диапазоне от О до 45° (включая О и 45). \n'
                  'Если это так, то поднимите перо черепахи.\n' +
                  '9. Напишите инструкцию if, которая применяет библиотеку черепашьей графики, чтобы определить, является ли цвет пера черепахи красным или синим. \n'
                  'Если это так, то установите размер пера 5 пикселов.\n' +
                  '10. Напишите инструкцию if, которая применяет библиотеку черепашьей графики, чтобы определить, находится ли черепаха в прямоугольнике. \n'
                  'Левый верхний угол прямоугольника находится в позиции (100, 100), а его правый нижний угол - в позиции (200, 200). Если черепаха в прямоугольнике, то спрячьте черепаху.\n' +
                  '0.Назад')
            exercise_1 = input()
            if exercise_1 == '1':
                print(task_1_1(101))
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '2':
                print(task_1_2(9))
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '3':
                print(task_1_3(10))
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '4':
                print(task_1_4())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '5':
                print(task_1_5())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '6':
                print(task_1_6())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '7':
                print(task_1_7(1))
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '8':
                print(task_1_8())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '9':
                print(task_1_9())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '10':
                print(task_1_10())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '0':
                break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '2':
        while True:
            print('1. Напишите цикл while, который позволяет пользователю ввести число. Число должно быть умножено на 1О, и результат присвоен переменной с именем product. \n'
                  'Цикл должен повторяться до тех пор, пока product меньше 100.\n' +
                  '2. Напишите цикл while, который просит пользователя ввести два числа. Числа должны быть сложены, и показана сумма. \n'
                  'Цикл должен запрашивать у пользователя, желает ли он выполнить операцию еще раз. Если да, то цикл должен повториться, в противном случае он должен завершиться.\n' +
                  '3. Напишите цикл for, который выводит приведенный ниже ряд чисел: О, 10, 20, 30, 40, 50, ..., 1000\n' +
                  '4. Напишите цикл, который просит пользователя ввести число. Цикл должен выполнить 1О итераций и вести учет нарастающего итога введенных чисел.\n' +
                  '5. Напишите цикл, который вычисляет сумму приведенного ниже числового ряда\n' +
                  '6. Перепишите приведенные ниже инструкции с использованием операторов расширенного присваивания.\n' +
                  '7. Напишите серию вложенных циклов, которые выводят 10 строк символов #. В каждой строке должно быть 15 символов #.\n' +
                  '8. Напишите программный код, который предлагает пользователю ввести положительное ненулевое число и выполняет проверку допустимости входного значения.\n' +
                  '9. Напишите программный код, который предлагает пользователю ввести число в диапазоне от 1 до 100 и проверяет допустимость введенного значения.\n' +
                  '0.Назад')
            exercise_2 = input()
            if exercise_2 == '1':
                print(task_2_1())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '2':
                print(task_2_2())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '3':
                print(task_2_3())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '4':
                print(task_2_4())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '5':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '6':
                print(task_2_6())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '7':
                print(task_2_7())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '8':
                print(task_2_8())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '9':
                print(task_2_9())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '0':
                break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '3':
        while True:
            print('1. День недели\n' +
                  '2. Площади прямоугольников\n' +
                  '3. Классификатор возраста\n' +
                  '4. Римские цифры\n' +
                  '5. Масса и вес\n' +
                  '6. Волшебные даты\n' +
                  '7. Цветовой микшер\n' +
                  '8. Калькулятор сосисок для пикника\n' +
                  '9. Цвета колеса рулетки\n' +
                  '10. Игра в подсчитывание монет\n' +
                  '11. Очки книжного клуба\n' +
                  '12. Реализация программного обеспечения\n' +
                  '13. Стоимость доставки\n' +
                  '14. Индекс массы тела\n' +
                  '15. Калькулятор времени\n' +
                  '16. Дни в феврале\n' +
                  '17. Диагностическое дерево проверки качевства Wi-Fi\n' +
                  '18. Селектор ресторанов\n' +
                  '0.Назад')
            exercise_3 = input()
            if exercise_3 == '1':
                print(task_3_1())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '2':
                print(task_3_2())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '3':
                print(task_3_3())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '4':
                print(task_3_4())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '5':
                print(task_3_5())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '6':
                print(task_3_6())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '7':
                print(task_3_7())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '8':
                print(task_3_8())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '9':
                print(task_3_9())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '10':
                print(task_3_10())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '11':
                print(task_3_11())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '12':
                print(task_3_12())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '13':
                print(task_3_13())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '14':
                print(task_3_14())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '15':
                print(task_3_15())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '16':
                print(task_3_16())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '17':
                print(task_3_17())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '18':
                print(task_3_18())
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_3 == '0':
                break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '4':
        while True:
            print('1. Сборщик ошибок\n' +
                  '2. Сожженные калории\n' +
                  '3. Анализ бюджета\n' +
                  '4. Пройденное расстояние\n' +
                  '5. Средняя толщина дождевых осадков\n' +
                  '6. Таблица соответствия между градусами Цельсия и градусами Фаренгейта\n' +
                  '7. Мелкая монета для зарплаты\n' +
                  '8. Сумма чисел\n' +
                  '9. Уровень океана\n' +
                  '10. Рост платы за обучение\n' +
                  '11. Потеря массы\n' +
                  '12. Вычисление факториала числа\n' +
                  '13. Популяция\n' +
                  '14. Напишите программу, которая применяет вложенные циклы для рисования этого узора\n' +
                  '15. Напишите программу, которая применяет вложенные циклы для рисования этого узора\n' +
                  '0.Назад')
            exercise_4 = input()
            if exercise_4 == '1':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '2':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '3':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '4':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '5':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '6':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '7':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '8':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '9':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '10':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '11':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '12':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '13':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '14':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '15':
                print()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')
                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_4 == '0':
                break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '0':
        sys.exit()

    else:
        print('Ошибка, введите правильное значение!')