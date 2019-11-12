import re
print()
print("Ця програма порівнює порівнює введені числа із певним іншим числом.")
print("Якщо немає такого числа яке рівне певному числу, то програма вичислює найбільшу різницю")
print()

def inp ():
    element = input('')
    if bool(re.match('^[+,-]{0,1}\\d+(\\.){0,1}\\d*$', element)):
        element = float(element)
    else:
        print('Error')
        inp()
    return element

def main(a,b,c,d):
    if a == d:
        print('a = d')
    elif b == d:
        print('b = d')
    elif c == d:
        print('c == d')
    else:
        if d - a > d - b and d - a > d - c:
            max = d - a
            print('max (d - a) = ', max)
        elif d - b > d - a and d - b > d - c:
            max = d - b
            print('max (d - b) = ', max)
        else:
            max = d - c
            print('max (d - c) = ', max)
