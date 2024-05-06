# define count vowels function
def count_vowels ():
    # ask user for an input
    original = input("What state do you live in? ")
    # create a variable for the vowels
    vowels = "aeiouAEIOU"
    # create a variable for the new string created by the loop/if statement
    new = ""
# loop each character from the input
    for char in original:
        # replace vowel with *
        if char in vowels:
            new += "1"
        # keep character if not vowel    
        else:
            new += "0"
    new = new.count("1")
    return new