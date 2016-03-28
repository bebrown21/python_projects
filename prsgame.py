# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# Function below converts names to their corresponding number
# If the name isn't recognized, an error is given

def name_to_number(name):
    if name == "rock":
        return "0"
    elif name == "Spock":
        return "1"
    elif name == "paper":
        return "2"
    elif name == "lizard":
        return "3"
    elif name == "scissors":
        return "4"
    else:
        print "Error: Name does not match available options: rock, paper, scissors, lizard, Spock."
    return 
# Funtion below converts number 0 - 4 to their corresponding name
# If the number isn't between 0 - 4 then an error is given
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Error: Number doesn't fall between 0 - 4."
    return 

# Function below prints the player and computer's choice   

def rpsls(player_choice): 
    
# Converting the player's guess to a number and printing the results

    player_number = name_to_number(player_choice)
    print "Player chooses " + player_choice
    
# Making computer's guess using random and converting it to a number
# and printing the results

    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
# Taking the difference of the Computer and Player's choice Modulo 5
# then determining the winner and printing the proper results

    difference = (int(comp_number) - int(player_number)) % 5
    if (difference == 1) or (difference == 2):
        print "Computer wins!"
    elif (difference == 3) or (difference == 4):
        print "Player wins!"
    else:
        print "Player and Computer Tie!"
        
# Adding a space between runs
    print 
    return

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")