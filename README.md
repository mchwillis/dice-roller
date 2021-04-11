# dice-roller
A simple dice roller to assist with all your TTRPG needs.

This dice roller allows users to input values for sides, number of dice, and modifiers to simplify your TTRPG sessions and reduce the number of physical dice necessary for your favorite Shadowrun campaign.
This was a personal project to help me better understand Python. Enjoy!

# Usage
The text will  first ask what game you are playing. You have the option to input `D&D`,`PF`, or `SR`, for Dungeons and Dragons, Pathfinder, and Shadowrun, respectively.
`What game are you playing [D&D/PF/SR]?`

This will determine the message displayed when a roll exceeds the threshold. This will be explained later. You are able to input whatever you would like, but if your input does not match one of the available options, you will receive the default response when the threshold is exceeded.

The text will then ask if you would like to roll the dice. 
`Would you like to roll the dice [Yes, sire/Nay]?`

You may respond with either `Yes, sire ` or `Nay`

You will then be asked `How many sides does your die have?`

Please resond with a number. If input is a string, you will receive an error and will need to run the script again.

The following three questions will be asked: `How many dice do you want to roll?`,`What is your modifier?`, and `What is your threshold for success or crit?`

Answer these questions with a digit as well.

If the number rolled exceeds the threshold, you will receive the sucess response. Success responses are provided below.

D&D `Critical!`

PF `Critical Threat!`

SR `Success!`

Other/Default `Cream of the crop!`

Once your dice have been rolled, you will be given the option to reroll your dice. This will allow you to roll with the same number, sides, and modifier that was previously input to avoid having to input the same data multiple times in succession.

The example below is rolling 5 D6 with a modifier of 0 and threshold of 3:

```
Rolling 5 D6 + 0...
2
2
2
5
Success!
4
Success!
Total: 15
Would you like to reroll your dice [y/n]?
```

If you reply with `n` you will be looped back to the beginning of the script.

To close the script, simply respond `Nay` when asked if you would like to roll the dice. A full example of the output and responses has been provided below.

```
What game are you playing [D&D/PF/SR]?
SR
Would you like to roll the dice [Yes, sire/Nay]?
Yes, sire
How many sides does your die have?
6
How many dice do you want to roll?
5
What is your modifier?
4
What is your threshold for success or crit?
3
Rolling 5 D6 + 0...
2
2
2
5
Success!
4
Success!
Total: 15
Would you like to reroll your dice [y/n]?
n
Would you like to roll the dice [Yes, sire/Nay]?
nay
Until we roll again, friend...
```
