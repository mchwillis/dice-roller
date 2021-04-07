import random

question = input ('Would you like to roll the dice [Yes, sire/Nay]?\n')

def roll(dice, sides, mod):
    print('Rolling ' + str(dice) + ' D' + str(sides) + ' + ' + str(mod) + '...')
    count = 0
    total = 0
    while count < dice:
        die = random.randint(1, sides)
        print(die)
        count = count + 1
        total = total + die
    totmod = total + mod
    print("Total:",(totmod))    

while question.lower() != 'nay':
        if question.lower() == 'yes sire' or question.lower() == 'yes, sire':
            sides = input("How many sides does your die have?\n")
            sides = int(sides)
            dice = input("How many dice do you want to roll?\n")
            dice = int(dice)
            mod = input("What is your modifier?\n")
            mod = int(mod)
            roll(dice, sides, mod)
            question = input ('Would you like to reroll your dice [y/n]?\n')
            while question != 'n':
                roll(dice, sides, mod)
                question = input ('Would you like to reroll your dice [y/n]?\n')
            
        else:
            print ('Invalid response. Please type "Yes, sire" or "Nay".')
        question = input ('Would you like to roll the dice [Yes, sire/Nay]?\n')

print('Until we roll again, friend...')


