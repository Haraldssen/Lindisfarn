from Human.Human import Human
from Human.Woman import Woman

woman = Woman(Human)

human = Human()

def q():
    return woman.sex
print(q())


def m():
    return human.stamina

print(m())