# dice-roller
A simple dice roller to assist with all your TTRPG needs.

This dice roller allows users to input values for sides, number of dice, and modifiers to simplify your TTRPG sessions and reduce the number of physical dice necessary for your favorite Shadowrun campaign.
This was a personal project to help me better understand Python. Enjoy!

# Usage
The text will first ask if you would like to roll the dice. 
`Would you like to roll the dice [Yes, sire/Nay]?`

You may respond with either `Yes, sire ` or `Nay`

You will then be asked `How many sides does your die have?`

Please resond with a number. If input is a string, you will receive an error and will need to run the script again.

The following two questions will be asked: `How many dice do you want to roll?` and `What is your modifier?`

Answer both of these questions with a digit as well.

Once your dice have been rolled, you will be given the option to reroll your dice. This will allow you to roll with the same number, sides, and modifier that was previously input to avoid having to input the same data multiple times in succession.

Your results will be displayed as:

```
Rolling 2 D6 + 12
2
6
Total: 20
Would you like to reroll your dice [y/n]?
```

If you reply with `n` you will be looped back to the beginning of the script.

To close the script, simply respond `Nay` when asked if you would like to roll the dice. A full example of the output and responses has been provided below.

```
Would you like to roll the dice [Yes, sire/Nay]?
Yes, sire
How many sides does your die have?
6
How many dice do you want to roll?
12
What is your modifier?
4
Rolling 12 D6 + 4...
5
1
6
3
6
5
3
3
3
2
5
3
Total: 49
Would you like to reroll your dice [y/n]?
n
Would you like to roll the dice [Yes, sire/Nay]?
Nay
Until we roll again, friend...
```
