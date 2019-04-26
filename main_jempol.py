# Main Jempol (Thumbs Game)
# Version 1.0.3 (26 April 2019)
# Created by Vino Tri Mulia
# Using Python 2

##################################

# What is Main Jempol?
# Main Jempol (Thumbs Game) is popular ice breaking game in Indonesia. It is played by several players (usually 3-7 people) circling around and facing each other. Here are the rules:
# 1. Initially, all players show both of their hand thumbs in down position (not raising).
# 2. Each player, in turns, shout a guessed number of raised thumbs by all players.
# 3. Simultaneously with the shout, all players may raise one or both thumbs, or no thumb at all.
# 4. If the player in turn guesses correctly, they can remove one thumb from the game. From now on, they may raise up to 1 thumb only.
# 5. Game ends when a player guesses correctly twice (both thumbs are removed from the game), and he/she is declared as winner.

# Note:
# - There is also variation where the game continues until there are two players left to defeat each other. However, we don't use that variation in this script.
# - This Python script simulates real Main Jempol. You will play with several bots that you choose in the beginning of game.
# - Each player (including you) are set as perfect logician. This means all players will not make invalid decision or valid decision with absolute failure.
# - Example of invalid decision: raising 3 thumbs, shouting 10 thumbs where there are only 8 thumbs, etc.
# - Example of valid decision with absolute failure: there are 2 players left with 2 thumbs, one player raises 1 thumb but shouts 4 thumbs.

##################################

# Importing library
import random, time

##################################

# Initialization (input for number of players, initial thumbs condition, and first turn)
# # Entering number of players
players_validator = 0
print "Please enter number of players (at least 2 players)."
while players_validator == 0:
    try:
        players = int(raw_input("Number of players: "))
        if players < 2:
            print "Please enter an integer that is greater than 1."
        else:
            time.sleep(0.3)
            print "{} players will play.".format(players)
            players_validator = 1
    except:
        print "Please enter an integer that is greater than 1."

# # Initializing thumbs
thumbs = []
for i in range(players):
    thumbs.append(2)

# # Drawing first turn
current_player = random.randint(0,players-1)
print ""
print "Players' indices start from 0, where you are the player number 0."
if current_player == 0:
    print "Based on random draw, player 0 (you) will start first.".format(current_player)
else:
    print "Based on random draw, player {} will start first.".format(current_player)
print ""

##################################
 
# Let's play!
while thumbs.count(0) == 0:
    if current_player == 0:
        print "It's your turn."
    else:
        print "Player {}'s turn.".format(current_player)
    print ""

    # # Raising the thumbs
    turn_thumbs = []
    for i in range(players):
        if i == 0:
            thumbs_validator = 0
            print "You have {} thumb(s) left.".format(thumbs[0])
            print "Please enter number of your raised thumb(s)."
            while thumbs_validator == 0:
                try:
                    raised_thumbs = int(raw_input("Number of your raised thumb(s): "))
                    if raised_thumbs < 0 or raised_thumbs > thumbs[0]:
                        print "Please enter an integer between 0 and {}.".format(thumbs[0])
                    else:
                        turn_thumbs.append(raised_thumbs)
                        time.sleep(0.3)
                        print "You will raise {} thumb(s).".format(raised_thumbs)
                        print ""
                        thumbs_validator = 1
                except:
                    print "Please enter an integer between 0 and {}.".format(thumbs[0])
        else:
            rand_thumbs = random.randint(0,thumbs[i])
            turn_thumbs.append(rand_thumbs)

    # # Making the guess
    min_guess = turn_thumbs[current_player]
    max_guess = sum(thumbs) - thumbs[current_player] + turn_thumbs[current_player]
    if current_player == 0:
        guess_validator = 0
        print "Please guess total number of raised thumb(s)."
        print "Based on number of your raised thumb(s), the possible answer is between {} and {}.".format(min_guess, max_guess)
        while guess_validator == 0:
            try:
                guess = int(raw_input("Total number of raised thumb(s): "))
                if guess < min_guess or guess > max_guess:
                    print "Please enter an integer between {} and {}.".format(min_guess, max_guess)
                else:
                    time.sleep(0.3)
                    guess_validator = 1
            except:
                print "Please enter an integer between {} and {}.".format(min_guess, max_guess)
    else:
        guess = random.randint(min_guess,max_guess)
        
    if current_player == 0:
        print "You guessed {}...".format(guess)
    else:
        print "Player {} guessed {}...".format(current_player, guess)
    time.sleep(0.3)

    # # Checking the guess
    if guess == sum(turn_thumbs):
        current_player_thumbs = thumbs[current_player]
        thumbs.pop(current_player)
        thumbs.insert(current_player,current_player_thumbs - 1)
        if current_player == 0:
            print "You guessed correctly!"
        else:
            print "Player {} guessed correctly!".format(current_player)
    else:
        print "Wrong guess! Total number of raised thumb(s) is(are) {}.".format(sum(turn_thumbs))
    print "Raised thumbs:"
    print turn_thumbs
    print ""

    # # Ending the turn
    current_player = (current_player + 1) % players
    print "Current thumbs condition:"
    print thumbs
    print ""
    print ""

##################################

# End game (not Avengers btw)    
winner = (current_player - 1) % players
time.sleep(0.3)
if winner == 0:
    print "You win!"
else:
    print "Player {} wins!".format(winner)
