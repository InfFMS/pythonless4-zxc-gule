# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
a=int(input())
def f(a):
    q=''
    b=''
    c=''
    d=''
    x=''
    z=''
    n=''
    if a//1000!=0:
        q=a//1000*'M'
    if (a%1000-a%100)==400:
        b='LC'
    elif (a%1000-a%100)==900:
        b='CM'
    elif (a%1000-a%100)//100>4:
        b='D'
    elif ((a%1000-a%100)//100)%5!=0:
        c = ((a % 1000 - a % 100) // 100) % 5 * 'C'
    if (a%100-a%10)//10 == 4:
        x = 'VX'
    elif (a%100-a%10)//10 == 9:
        x = 'XC'
    elif (a % 100 - a % 10) // 10 > 4:
        d = 'L'
    elif (a%100-a%10)//10!=0:
        x=((a%100-a%10)//10)%5*'X'
    if a%10>4 and a%10!=4 and a%10!=9:
        z='V'
    if a%10==4:
        n='IV'
    elif a%10==9:
        n='IX'
    elif a%10!=0:
        n=a%5*'I'
    print(q+b+c+d+x+z+n)
    return ''
print(f(a))