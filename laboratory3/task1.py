import re
import string

print()
print('Лабораторна робота 3')
print('Варіант21. Програма для виводження латинського алфавіту без літер, які не належать будь-якому рядку S1 і S2')
print('Стефанишин Н. І., КМ-91')
print()

def inp(word):

    if bool(re.match('^[a-zA-Z]+$', word)):
        word1_1 = []
        for j in range(len(word)):
            word1_1.append(word[j])
    else:
        print('Error')
        inp()
    return word1_1

def main (word_delete):
    start = 0
    word_delete = list(word_delete)
    finish = len(word_delete)
    while start < finish:
        k = word_delete.count(word_delete[start])
        while k > 1:
            word_delete.remove(word_delete[start])
            k -= 1
            finish -= 1
        start += 1
    alphabet = list(string.ascii_letters)
    for i in range(len(word_delete)):
        alphabet.remove(word_delete[i])
        alphabet_array = ''.join(alphabet)
    print('result:', alphabet_array)
    return alphabet_array

flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

while flag != 'n' :
    word1 = input('1 line:')
    inp(word1)
    word2 = input('2 line:')
    inp(word2)
    word_delete = word1 + word2
    main(word_delete)

    flag = input('Натисніть "Enter" для запуску програми або "n" для завершення тестування ')

else:
    print('Допобачення <3')