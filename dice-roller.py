import random

#Dice roll function
def roll(dice, sides, mod):
    print('Rolling ' + str(dice) + ' D' + str(sides) + ' + ' + str(mod) + '...')
    count = 0
    total = 0
    while count < dice:
        die = random.randint(1, sides)
        print(die)
        if die >= thresh and game.lower() == 'dnd' or die >= thresh and game.lower() == 'd&d':
            print('Crit!')
        elif die >= thresh and game.lower() == 'pf':
            print('Critical threat!')
        elif die >= thresh and game.lower() == 'sr':
            print('Success!')
        elif die >= thresh and game.lower() !='dnd' or die >= thresh and game.lower() !='d&d' or die >= thresh and game.lower() !='pf' or die >= thresh and game.lower() !='sr':
            print('Cream of the crop!')
        count = count + 1
        total = total + die
    totmod = total + mod
    print("Total:",(totmod)) 
    
game = input('What game are you playing [D&D/PF/SR]?\n')
question = input ('Would you like to roll the dice [Yes, sire/Nay]?\n')
while question.lower() != 'nay':
        if question.lower() == 'yes sire' or question.lower() == 'yes, sire':
            sides = input('How many sides does your die have?\n')
            while True:
                try:
                    sides = int(sides)
                    break
                except ValueError:
                    print ("That's not a whole number, silly!")
                sides = input('How many sides does your die have?\n')
            dice = input('How many dice do you want to roll?\n')
            while True:
                try:
                    dice = int(dice)
                    break
                except ValueError:
                    print ("That's not a whole number, silly!")
                dice = input ('How many dice do you want to roll?\n')
            mod = input("What is your modifier?\n")
            while True:
                try:
                    mod = int(mod)
                    break
                except ValueError:
                    print ("That's not a whole number, silly!")
                mod = input('What is your modifier?\n')
            thresh = input('What is your threshold for success or crit?\n')
            while True:
                try:
                    thresh = int(thresh)
                    break
                except ValueError:
                    print ("That's not a whole number, silly!")
                sides = input('What is your threshold for success or crit?\n')
            roll(dice, sides, mod)
            question = input ('Would you like to reroll your dice [y/n]?\n')
            while question != 'n':
                roll(dice, sides, mod)
                question = input ('Would you like to reroll your dice [y/n]?\n')
        else:
            print ('Invalid response. Please type "Yes, sire" or "Nay".')
        question = input ('Would you like to roll the dice [Yes, sire/Nay]?\n')
print('Until we roll again, friend...')


