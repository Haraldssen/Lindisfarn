import random

class Human:

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money=0):
        self.sex = 'male'
        self.name = name
        self.soname = soname
        self.age = age
        self.money = money
        self.stamina = 150
        self.moral = 50

    def getName(self):
        return self.sex + ' ' + self.name + ' ' + self.soname

    def setName(self, name=None, soname=None):
        if name:
            self.name = name
        if soname:
            self.soname = soname

    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina += 10
            print(self.name, 'я покушаль! (=', 'денег осталось', self.money, 'зато поправился до', self.stamina)
        else:
            print(self.name, 'Нету денег! :(')

    def beer(self):
        if self.money > 0:
            self.money -= random.randint(0, 4)
            self.stamina -= 20
            self.moral += 10
            print(self.name, 'зачем пил! :(', 'денег осталось', self.money, 'ощущения на', self.stamina - 150)
        else:
            print(self.name, 'займи, но выпей')

    def work(self):
        self.money += 5
        self.stamina -= 10
        self.moral -= 5
        print(self.name, 'хорошо поработал')
        return ['money', 'moral', 'stamina']

