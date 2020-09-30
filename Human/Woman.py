import random

from Human.Human import Human

class Woman(Human):

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money = 0):
        super().__init__(name, soname, age, money)
        self.sex = 'female'
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
#здесь я хотел привязать money Марины к money Артема,
# чтобы при расходах Марины тратились деньги Артема, как в жизни.
    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina += 5
            print(self.name, 'я жирная! (=', self.money, self.stamina)
        else:
            print(self.name, 'Совсем нету денег на ноготочки :(')

    def shopping(self):
        if self.money > 0:
            self.money -= random.randint(1, 4)
            self.moral += random
            print(self.name, 'Люська позеленеет :)', self.money, self.moral)
        else:
            print(self.name, 'Связалась с нищебродом')

