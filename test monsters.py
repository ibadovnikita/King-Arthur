import random
HP=100
eHP=10
enemy = random.randint(0, 2)
def enemys(enemy):
    if enemy == 0:
        eHP = 100
        edamage = 10
    elif  enemy == 1:
        eHP = 200
        edamage = 5
    elif enemy == 2:
        eHP = 50
        edamage = 20
    return eHP, edamage
def fight(HP, eHP):
    import random
    eHP, edamage =enemys(enemy)
    N=1
    while HP > 0 and eHP > 0:
        print('Номер хода:', N)
        roll = random.randint(-2, 10)
        if roll >= 1:
                damage = random.randint(0, 20)
                eHP = eHP - damage
                if eHP > 0:
                    print("У врага осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
        else:
                print("Ты промахнулся")
        if eHP > 0:
            eroll= random.randint(-2, 10)
            if eroll >= 1:
                    
                    HP = HP - edamage
                    if HP > 0:
                        print("У тебя осталось ", HP, " ХП")
                    else:
                        print("У тебя не осталось ХП")
            else:
                    print("Враг промахнулся")
        else:
            break
        N=N+1
    if HP <= 0:
        print('Ты погиб')
    if eHP <= 0:
        print('Враг погиб')
    return HP, eHP
fight(HP, eHP)
