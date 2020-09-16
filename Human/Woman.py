from Human.Human import Human


class Woman(Human):

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money=0):
        super().__init__(name, soname, age, money)
        self.sex  = 'female'
        self.stamina = 100

    @staticmethod
    def reproduce(father=None, mother=None):
        if father and mother:
            if type(father) == Human and type(mother) == Woman:
                print('можно размножаться')
                return Human()
            else:
                print('Алярма!')
                return None
        print('не хватает одного из родителей')
        return None

    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina += 5
            print(self.name, 'я покушала! (=', self.money, self.stamina)
        else:
            print(self.name, 'Совсем нету денег на ноготочки :(')