import re
print('Стефанишин Н. І., КМ-91')
print()
print('Лабораторна робота 1. Варіант21. Завдання 1.')
print('Програма підносить число до степення не використовуючи ніяких арифметичних операцій, крім множення')
print()

def main ():
    element = input('Введіть число а=')
    if bool(re.match('^[+,-]{0,1}\\d+(\\.){0,1}\\d*$', element)):
        element_2 = float(element) * float(element)
        element_4 = element_2 * element_2
        print('a^4=',round(element_4,16))
        element_6 = element_2 * element_4
        print('a^6=', round(element_6,5))
        element_3 = element_2 * float(element)
        element_15 = element_6 * element_6 * element_3
        print('a^15=', round(element_15,5))

    else:
        print('Error')
        main()

flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

while flag != 'n' :
    main()
    flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

else:
    print('Допобачення <3')