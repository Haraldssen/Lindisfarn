'''# нахождение корня квадратного уравнения через дискриминанту
# a * х * х + b * x + c = 0
# D = b * b - 4 * a * c
# если D > 0, то x = (-b + sqrt(D)) / (a * 2), Х = (-b - sqrt(D)) / (a * 2)
# если D = 0, то x = - b / (a * 2)
# если D < 0, то корней нет

a = 3
b = 10
c = 1

D = (b * b) - (4 * a * c)

import math

d = math.sqrt(D)

if D > 0:
    x = ((b + d) / (a * 2)) , 'и', ((-b - d) / (a * 2))
    print(x)
if D == 0:
    x = ((- b / (a * 2))
    print(x)
if D < 0:
    print('корней нет')

# объявление функции
'''
import math

k = 45
b = 9

c = 90

def lineEqual(a, b):
    if not a == 0:
        return [-b / a]
    return []


def squareEqual(a, b, c):
    #если вдруг уравнение оказалось линейным
    if a == 0:
        return lineEqual(b, c)
    D = b ** 2 - 4 * a * c
    if D == 0:
        return [-b / (2 * a)]
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    return []

print(lineEqual(1, 2))
