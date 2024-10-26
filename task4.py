# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
a=int(input())
b=int(input())
def f(a,b):
    m=0
    while m!=a:
        if a>b:
            a=a-b
        elif a<b:
            b=b-a
        if a==b:
            m=a
            print('НОД:',m)
            break
    return ''
print(f(a,b))