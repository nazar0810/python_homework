import re
print()
print('лабораторна робота 2')
print('Варіант21. Програма для знаходження найменшого цілого числа за певних умов')
print('Стефанишин Н. І., КМ-91')
print()

def main():
    element = input('Введіть ціле число:')
    if bool(re.match('^[1-9]+$', element)):
        element = int(element)
        if element > 1:
            K = 1
            sum = 1
            while sum <= element:
                K += 1
                sum += K
            sum -= K
            K -= 1
            print('K=', K)
            print('Sum=', sum)
        else:
            print('Зауваження: N має бути цілим числом і більше 1')
            main()

    else:
        print('Зауваження: N має бути цілим числом і більше 1')
        main()

flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

while flag != 'n' :
    main()
    flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

else:
    print('Допобачення <3')