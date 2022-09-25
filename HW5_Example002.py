# Задача 2.

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи:
# На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.

# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"



from os import system
from random import randint
system ('cls')
import Base




def candy_game_man(total_candies:int,max_candies:int):
    '''
    Игра в конфеты. Игра с двумя игроками.  Проигрывает тот , кто взял последнюю конфету. 
    total_candies - общее количество конфет участвующее в игре 
    max_candies - максимальное количество конфет, которые можно взять за один ход.
    '''

    man_work = randint(1,2)

    print (f'Игру начинает участник c №: {man_work}')


    while total_candies!=1:
        print (f'Ход игрока с № {man_work}')
        if max_candies>=total_candies:
            max_candies=total_candies-1
        candies = Base.check_numberMinMax(1,max_candies,f'Осталось {total_candies} конфет. Сколько будем забирать ( от 1 до {max_candies}):')
        total_candies-=candies
        if total_candies==1:
            print(f'Осталось одна конфета. Выиграл игрок с номером {man_work}')
        if man_work==1:
            man_work=2
        else:
            man_work=1
    

def candy_game_bot(total_candies:int,max_candies:int,name_man:str='Игрок',name_bot:str='Бот'):
    '''
    Игра в конфеты. Игра с ботом.  Проигрывает тот , кто взял последнюю конфету. 
    total_candies - общее количество конфет участвующее в игре 
    max_candies - максимальное количество конфет, которые можно взять за один ход.
    name_man - имя игрока
    name_bot - имя бота 
    '''
    mw =randint(1,2)
    
    if mw == 1:
        man_work=name_man
    else:
        man_work=name_bot

    print (f'Игру начинает : {man_work}')


    while total_candies!=1:
        print (f'Ходит: {man_work}')
        if max_candies>=total_candies:
            max_candies=total_candies-1
        if man_work==name_man:
            candies = Base.check_numberMinMax(1,max_candies,f'Осталось {total_candies} конфет. Сколько будем забирать ( от 1 до {max_candies}):')
        else:
            print(f'Осталось {total_candies} конфет')
            candies=randint(1,max_candies)
            print (f'{man_work} взял {candies} конфет ')
        total_candies-=candies
        if total_candies==1:
            print(f'Осталось одна конфета. Выиграл {man_work}')
        if man_work==name_man:
            man_work=name_bot
        else:
            man_work=name_man

def candy_game_bot_intellect(total_candies:int,max_candies:int,name_man:str='Игрок',name_bot:str='Бот'):
    '''
    Игра в конфеты. Игра с интеллектуальным ботом. Проигрывает тот , кто взял последнюю конфету. 
    total_candies - общее количество конфет участвующее в игре 
    max_candies - максимальное количество конфет, которые можно взять за один ход.
    name_man - имя игрока
    name_bot - имя бота 
    '''
    
    def intellect(total_candies,max_candies):
        number=1
        if total_candies//max_candies>1:
            if total_candies%(max_candies+2)==0:
                number = 1
            elif total_candies%(max_candies+2)==(max_candies+1):
                number = 1
            else:
                number=total_candies%(max_candies+2)
        else:
            if total_candies%(max_candies+2)==0:
                number = 1
            elif total_candies%(max_candies+2)==(max_candies+1):
                number = max_candies
            else:
                number=total_candies%(max_candies+2)

        return number
    
    mw =randint(1,2)
    
    if mw == 1:
        man_work=name_man
    else:
        man_work=name_bot

    print (f'Игру начинает : {man_work}')


    while total_candies!=1:
        print (f'Ходит: {man_work}')
        if max_candies>=total_candies:
            max_candies=total_candies-1
        if man_work==name_man:
            candies = Base.check_numberMinMax(1,max_candies,f'Осталось {total_candies} конфет. Сколько будем забирать ( от 1 до {max_candies}):')
        else:
            print(f'Осталось {total_candies} конфет')
            candies=intellect(total_candies,max_candies)
            print (f'{man_work} взял {candies} конфет ')
        total_candies-=candies
        if total_candies==1:
            print(f'Осталось одна конфета. Выиграл {man_work}')
        if man_work==name_man:
            man_work=name_bot
        else:
            man_work=name_man


print('Игра в конфеты:\n1 - Два игрока. \n2 - Игра с ботом. \n3 - Игра с интеллектуальным ботом.')

game_selection = Base.check_numberMinMax(1,3, 'Введите № игры:')

total_candies = Base.check_number_more(21,'Введите общее количество конфет, которые будут использовать в игре (не менее 21): ')  # Всего конфето

max_number = total_candies//3

max_candies = Base.check_numberMinMax( 3,max_number, f'Введите максимальное количество конфет, которые можно забрать за 1 шаг ( В диапазоне от 3 до {max_number}): ')

if game_selection==1:
    candy_game_man(total_candies,max_candies)
elif game_selection==2:
    candy_game_bot(total_candies,max_candies)
else:
    candy_game_bot_intellect(total_candies,max_candies)