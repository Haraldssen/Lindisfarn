'''
from formulaEquation import Equation

equal = Equation

arr = equal.square(0, 1, 6, 2)
for i in range(len(arr)):
    print('x =', i)
'''

from Human.Human import Human
from Human.Woman import Woman

a = Human('Vovkas', 'Pomeloffs')
b = Human('Artem', 'Rozhkoff')
c = Woman('Marina', 'Petrova')
d = Woman.reproduce(a, c)

b.work()
b.eat()
c.eat()

print(a.getName(), b.getName(), c.getName(), d.getName())

