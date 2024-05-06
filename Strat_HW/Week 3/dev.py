# 1A.
# define count vowel function
def count_vowels ():
    # ask user for an input
    original = input("What state do you live in? ")
    # create a variable for the vowels
    vowels = "aeiouAEIOU"
    # create a variable for the new string created by the loop/if statement
    new1 = ""
    new2 = ""
    new3 = ""
# loop each character from the input
    for char in original:
        # replace vowel with 1
        if char in vowels:
            new1 += "1"
        # replace non-vowel with 0    
        else:
            new1 += "0"
    # variable is now the count of vowels        
    new1 = new1.count("1")
    # select each character from user input
    for char in original:
        # add vowels to the new2 variable
        if char in vowels:
            new2 += char
        # add consonants to the new3 variable    
        else:
            new3 += char
    # make list
    my_list = [original,new1, new2, new3]
    return my_list

print(count_vowels())

# 1b. 
# import math module
import math
# define fixed-coupon bond pricer
def bond_pricer():
    # variable for notional value (what bond issuer repays at maturity)
    N = input("What is the notional value? ")
    # make N a float
    N = float(N)
    # the period size as a fraction of a year; will be a float value
    dt = input("What is the period size? ")
    # make dt a float
    dt = float(dt)
    # interest rate input
    r = input("What is the rate? ")
    # make the input a float
    r = float(r)
    # make negative r variable
    neg_r = -r
    # periodic interest payment by bond issuer to holder (this is a fixed $25 for this particular bond)
    CF = input("What is the coupon? ")
    # make CF a float
    CF = float(CF)
    # length of time (in years) until the bond matures
    T = input("What is the term in years? ")
    # make T a float
    T = float(T)

    # determine number of tranches
    num_tranches = T / dt
    # create tranche variable
    tranche = 0
    tranche = float(tranche)
    # create variable for sum of tranche PV
    sum_tranche = 0
    sum_tranche = float(sum_tranche)
    # while loop that iterates through each tranche
    while tranche < (num_tranches - 1):
    # add 1 to tranche variable per iteration (the number will specify which tranche is being calculated)    
        tranche += 1
    # create time variable for calc
        time = tranche * dt
    # find pv of tranche
        tranche_pv = math.exp(neg_r * time) * CF
    # sum tranche PVs except for final tranche
        sum_tranche += tranche_pv
    # create time variable for final tranche    
    last_tranche_time = (num_tranches * dt)
    # find pv of final tranche
    last_tranche_pv = math.exp(neg_r * last_tranche_time) * (CF + N)
    # sum the final tranche and the value of the tranches from the loop
    final_sum = sum_tranche + last_tranche_pv
    # round to 2 decimal places
    final_sum = round(final_sum, 2)
    return final_sum
# print the final result
print(f"Bond Price: ${bond_pricer()}")

# 2a

# import random module
import random

# player 1 name
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

# generate 2 random numbers between 1 and 6 for player 1
player1_roll1 = random.randint(1, 6)
player1_roll2 = random.randint(1, 6)
# sum the 2 rolls
player1_sum = player1_roll1 + player1_roll2

# generate 2 random numbers betwen 1 and 6 for player 2
player2_roll1 = random.randint(1,6)
player2_roll2 = random.randint(1,6)
# sum the 2 rolls
player2_sum = player2_roll1 + player2_roll2

# if statement to determine the winner
def winner():
    if player1_sum > player2_sum:
        print(f"{player1} wins!")
    else:
        print(f"{player2} wins!")
# print player 1 score
print(f"{player1}'s score: {player1_sum}")
#print player 2 score
print(f"{player2}'s score: {player2_sum}")
# call winner finction which will say who the winner is
winner()


        
        



