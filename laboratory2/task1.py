import re
print()
print('лабораторна робота 2')
print('Варіант21. Програма для обчислення значення функції в залежності від змінної "x"')
print('Стефанишин Н. І., КМ-91')
print()

def inp ():
    element = input( )
    if bool(re.match('^[+,-]{0,1}\\d+(\\.){0,1}\\d*$', element)):
        element = float(element)
    else:
        print('Error')
        inp()
    return element

def main(element_1, element_2):
    i = 1
    result = 0
    while i <= element_2:
        result += ((2 * element_1 ** i - 1) / (element_2 - 1))
        i += 1
    print('F(x)=', round(result, 2))

flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

while flag != 'n' :
    print('x:')
    x = inp()
    print('n:')
    n = inp()
    main(x, n)

    flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

else:
    print('Допобачення <3')