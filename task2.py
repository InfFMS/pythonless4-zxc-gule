# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
num=int(input())
def f(num):
    a=num%10
    b=(num%100-num%10)//10
    c=''
    d=''

    if a==1:
        d='один'
    elif a==2:
        d='два'
    elif a ==3:
        d = 'три'
    elif a ==4:
        d = 'четыре'
    elif a ==5:
        d = 'пять'
    elif a ==6:
        d = 'шесть'
    elif a ==7:
        d = 'семь'
    elif a ==8:
        d = 'восемь'
    elif a==9:
        d='девять'
    elif num==10:
        print('десять')
    elif num ==11:
        print('одинадцать')
    elif num ==12:
        print('двенадцать')
    elif num ==13:
        print('тринадцать')
    elif num ==14:
        print('четырнадцать')
    elif num ==15:
        print('пятнадцать')
    elif num ==16:
        print('шестнадцать')
    elif num ==17:
        print('семнадцать')
    elif num ==18:
        print('восемнадцать')
    elif num ==19:
        print('девятнадцать')
    if b==2:
        c='двадцать'
    elif b == 3:
        c = 'тридцать'
    elif b == 4:
        c = 'сорок'
    elif b == 5:
        c = 'пятьдесят'
    elif b == 6:
        c = 'шестьдесят'
    elif b == 7:
        c = 'семьдесят'
    elif b == 8:
        c = 'восемьдесят'
    elif b == 9:
        c = 'девяносто'
    if 10>num or num>19:
        if c=='':
            print(c)
        else:
            print(c,d)
    return ''
print(f(num))