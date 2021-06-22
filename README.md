# dice-roller
A simple dice roller to assist with all your TTRPG needs.

This dice roller allows users to input values for sides, number of dice, and modifiers to simplify your TTRPG sessions and reduce the number of physical dice necessary for your favorite Shadowrun campaign.
This was a personal project to help me better understand Python. Enjoy!

# Usage
The terminal will  first ask what game the user is playing. The user will be suggested the input options `D&D`,`PF`, or `SR`, for Dungeons and Dragons, Pathfinder, and Shadowrun, respectively.
`What game are you playing [D&D/PF/SR]?`

This will determine the message displayed when a roll exceeds the threshold. The user is able to input whatever they would like, but if their input does not match one of the available options, they will receive the default response when the threshold is exceeded.

The terminal will then ask if the user would like to roll the dice. 
`Would you like to roll the dice [Yes, sire/Nay]?`

The user may respond with either `Yes, sire ` or `Nay`. If the user's input does not match either option, they will be asked the same question again.

The terminal will then ask `How many sides does your die have?`.

The user should resond with an integer. If the input is a string or float, the user will receive an error message and will be asked for a whole number.
```
How many sides does your die have?
j
That's not a whole number, silly!
How many sides does your die have?
```

The following three questions will be asked: `How many dice do you want to roll?`,`What is your modifier?`, and `What is your threshold for success or crit?`.

The input provided by the user for these three questions are also checked to ensure they are integers. As above, if the input is a string or float, the user will receive an error message and will be asked again for a whole number. Once all questions are answered, the die(dice) will be rolled and totals calculated.

If the number rolled exceeds the threshold, the user will receive a sucess response. Success responses are provided below.

D&D `Critical!`

PF `Critical Threat!`

SR `Success!`

Other/Default `Cream of the crop!`

Once the die(dice) have been rolled, the user will be given the option to reroll their dice. This will allow the user to roll with the same number, sides, and modifier that was previously input to avoid having to input the same data multiple times in succession.

The example below is rolling 9 D6 with a modifier of 0 and threshold of 5 with `SR` selected as the game being played:

```
Rolling 9 D6 + 0...
5 Success!
3
4
3
3
3
3
4
1
Total: 29
Would you like to reroll your dice [y/n]?
```

When prompted to reroll, if the user replies with `n` they will be looped back to the beginning of the script.

To close the script, the user would simply respond `Nay` when asked if they would like to roll the dice. A full example of the output and responses has been provided below.

```
What game are you playing [D&D/PF/SR]?
SR
Would you like to roll the dice [Yes, sire/Nay]?
Yes, sire
How many sides does your die have?
6
How many dice do you want to roll?
9
What is your modifier?
0
What is your threshold for success or crit?
5
Rolling 9 D6 + 0...
5 Success!
3
4
3
3
3
3
4
1
Total: 29
Would you like to reroll your dice [y/n]?
n
Would you like to roll the dice [Yes, sire/Nay]?
Nay
Until we roll again, friend...
```
