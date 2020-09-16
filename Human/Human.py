class Human:

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money=0):
        self.sex = 'male'
        self.name = name
        self.soname = soname
        self.age = age
        self.money = money
        self.stamina = 150

    def __del__(self):
        print('экземпляр уничтожен', self.name)

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
            print(self.name, 'я покушаль! (=', self.money, self.stamina)
        else:
            print(self.name, 'Нету денег! :(')

    def work(self):
        self.money += 5
        self.stamina -= 10