# import random
# define a function to roll the dice
# create a dictionary that will have drawings of the dice
# create a dictionary that will have the values of the dice

import random

dice = '⚀⚁⚂⚃⚄⚅'


def role_dice():
    roll = input('Roll the dice ya / tidak.? : ')
    while roll in ['Yes', 'yes', 'ya', 'y', 'yep']:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print('Dice rolled:{} and {}'.format(dice[dice_1], dice[dice_2]))
        roll = input('role again.? ')


role_dice()
