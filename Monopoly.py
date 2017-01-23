# Models a Single Monopoly Player's Tour Around a board multiple Times
# @Author David Awad

import random
from random import shuffle, randint

# simulate 10^5 games
games  = 10**5

# simulate average of finish turns per game
finish = 35

# create array of all squares on the board
squares = [0]*40

# track the number of games so far
games_finished = 0

while games_finished < games:

    # set of community chest cards
    master_chest = [0,40,40,40,40,10,40,40,40,40,40,40,40,40,40,40]
    chest = [i for i in master_chest]
    shuffle(chest)

    # set of chance cards
    master_chance = [0,24,11,'U','R',40,40,'B',10,40,40,5,39,40,40,40]
    chance = [i for i in master_chance]
    shuffle(chance)

    doubles  = 0
    position = 0
    turns = 0

    while turns < finish:
        d1, d2   = randint(1, 6), randint(1, 6)
        diceroll = d1 + d2

        # increment number of doubles
        if d1 == d2: doubles += 1
        else: doubles = 0

        # go to jail
        if doubles >= 3: position = 10

        else:
            position = (position + diceroll) % 40

            # Chance Card
            if position in [7,22,33]:
                chance_card = chance.pop(0)
                if len(chance) == 0: # chance deck is spent
                    chance = [i for i in master_chance]
                    shuffle(chance)
                if chance_card != 40:

                    if isinstance(chance_card, int):
                        position = chance_card
                    elif chance_card == 'U': # utilities
                        while position not in [12,28]:
                            position = (position + 1)%40

                    elif chance_card == 'R': # railroad
                        while position not in [5,15,25,35]:
                            position = (position + 1)%40

                    elif chance_card == 'B': # back 3 spaces
                        position = position - 3

            # Community Chest
            elif position in [2,17]:
                chest_card = chest.pop(0)
                if len(chest) == 0:
                    chest = [i for i in master_chest]
                    shuffle(chest)
                if chest_card != 40: position = chest_card

            # Go to jail
            if position == 30: position = 10

        squares.insert(position, (squares.pop(position)+1))
        turns += 1

    games_finished += 1

print(squares)
# a player lands on a space (finish_order * games) times
