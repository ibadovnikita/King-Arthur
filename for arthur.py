import random
HP=100
eHP=10
#СHead - coefficient Head- переменная на которую будет множиться урон в голову (В дальнейшем нужно будет перевести в статы врагов и возможно оружия)
#CChest - коэф грудной клетки (торса)
#CHand - коэф рук
#CFoot - коэф ног
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
    enemys(enemy)
    eHP,edamage = enemys(enemy)
    #СHead - coefficient Head- переменная на которую будет множиться урон в голову (В дальнейшем нужно будет перевести в статы врагов и возможно оружия)
    #CChest - коэф грудной клетки (торса)
    #CHand - коэф рук
    #CFoot - коэф ног
    CHead = 3
    CСhest = 1
    CHand =  1
    CFoot = 1
    N=1
    while HP > 0 and eHP > 0:
        print('Номер хода:', N)
        answer = int(input(" Куда вы хотити ударить 1 = голова,2 = тело, 3 = ноги,4 = руки: "))
        print(answer)
        if answer == 2:
            roll = random.randint(0, 100)
            if roll >= 25:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CСhest
                if eHP > 0:
                    print("Ты ударил врага в торс,  у него осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
            else:
                print("Ты промахнулся")
        elif answer == 1:
            roll = random.randint(0, 100)
            if roll >= 80:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CHead 
                if eHP > 0:
                    print("Своим мощным ударом в голову ты оставил врагу жалкие", eHP, " ХП")
                else:
                    eHP=0
                    print("Своим ударом Сайтамы ты низвел до атомов врага")
            else:
                print("Ты промахнулся")
        elif answer == 3: 
            roll = random.randint(0, 100)
            if roll >= 60:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CFoot
                if eHP > 0:
                    print("Ты ударил врага в ноги,  у него осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
            else:
                print("Ты промахнулся")
        elif answer == 4:
            roll = random.randint(0, 100)
            if roll >= 60:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CHand
                if eHP > 0:
                    print("Ты ударил врага в руки,  у него осталось ", eHP, " ХП")
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
