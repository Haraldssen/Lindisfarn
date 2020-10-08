'''
from formulaEquation import Equation

equal = Equation

arr = equal.square(0, 1, 6, 2)
for i in range(len(arr)):
    print('x =', i)


from Human.Human import Human
from Human.Woman import Woman

player1 = Human('Vovkas', 'Pomeloffs')
player2 = Human('Artem', 'Rozhkoff')
player3 = Woman('Marina', 'Petrova')
collaboration = Woman.reproduce(player1, player3)

player2.work()
player2.eat()
player2.beer()
player3.eat()
player3.shopping()

print(player1.getName(), player2.getName(), player3.getName(), collaboration.getName())


'''


#мой первый декоратор
# йуй сос мыслом!
def decorator(func):
    print('Я - декоратор, который умеет сохранять свое состояние!')

    def func2():
        print('код, который исполнится перед вызовом')
        func()
        print('код, который исполнится после вызова')
    return func2


@decorator
def func3():
    print('А я еще одна функция!')


#func3()

#возведение в квадрат
def square(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

@square
def add(a, b, c):
    return a + b + c

print(add(3, 7, -2))

#возведение в степень
def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(power)
            i = 0
            result = 1
            while i < power:
                result *= func(*args, **kwargs)
                i +=1
            return result
        return wrapper
    return decorator

@pow(power=3)
def add(a, b, c):
    return a + b + c

print(add(3, 7, 0))


