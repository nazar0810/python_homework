from math import log1p
import re
print("Програма знаходить та виводить розв'язок cистеми рівнянь в залежності від значення зміX")
print("Стефанишин Н. І.")

def main():
    element = input('X=')
    if bool(re.match('^[+,-]{0,1}\\d+(\\.){0,1}\\d*$', element)):
        element = float(element)
        if element <= -3:
            result = -element ** 2 - 1.1 * element + 9
            print('F(x) = ', round(result, 1))
        else:
            result = log1p(element + 3) / (element ** 2 + 9)
            print('F(x) = ', round(result, 2))
    else:
        print('Error')
        main()

flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

while flag != 'n' :
    main()
    flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

else:
    print('Допобачення <3')
