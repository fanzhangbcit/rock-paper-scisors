# Game: Rock, Paper, Scissors
#In this project you will make a Rock, Paper, Scissors game and play against the computer. The winner is decided by these rules:
#* Rock blunts scissors
#* Paper covers rock
#* Scissors cut paper

# Author: Fan Zhang

import random
import re
import warnings

rpsList=["r", "p", "s"]
rpsDict={"r":"rock","p":"paper","s":"scissors"}

### The game
def rps_play():
    playFlag = 1;
    # - First, let the player choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’;
    print("Game: rock(r), paper(p), scissors(s). Type 'exit' to leave.")
    while playFlag:
        player=input("Please enter your choice r, p, s:")
        if re.match("^[rsp]$", player):
            # xform r,p,s to 0,1,2
            player_index = rpsList.index(player)
            playFlag=0
            return player_index
        elif re.match("^exit$", player):
            print("\n---Thanks for playing, Bye!")
            playFlag=0
            return -1
        else:
            warnings.warn(UserWarning("Warning - User input was not r, p or s..."))


### - Then computers turn;
def rps_computer():
    computer_index=random.randint(0,2)
    return computer_index

### Compare the computer and player choice
def rps_compare(player,computer):
    if player == -1:
        return-2
    else:
        print ("\n*Player chose " + rpsDict[rpsList[player]])
        print ("\n*Computer chose " + rpsDict[rpsList[computer]])

    if (computer+1) % 3 == player:
        print("\n---Player wins!")
        return -1
    elif(computer==player):
        print("\n---Its a Draw!")
        return 0
    else:
        print("\n---Computer wins!")
        return 1

# - Decide game win, lose or draw, print choice of both sides
if __name__ == '__main__':
    rps_compare(rps_play(),rps_computer())