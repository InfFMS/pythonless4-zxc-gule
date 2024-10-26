# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
a=int(input())
b=int(input())
c=int(input())
def f(a,b,c):
    if a<b+c and b<a+c and c<b+a:
        print('True')
    else:
        print('False')
    return ''
print(f(a,b,c))