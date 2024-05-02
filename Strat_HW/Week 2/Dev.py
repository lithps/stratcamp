# 1a. Tuples are immutable; the contents and the order cannot be altered or manipulated

# 1b. List of tuples

list_1b = [(1001),(7 * 10), (10 + 3), (1 - 6)]
greatest = max(list_1b)

print(f"{greatest} is the greatest and bestest tuple.")

# 2a. Sets are mutable, but have no duplicates. They are enclosed curly brackets.

# 2b. Convert list to set

list_2b = [1,2,3,3,4,1]
print(set(list_2b))

# 2c. Common elements of three sets

set_a = {2,4,6,8,10}
set_b = {3,6,9,12,15}
set_c = {1,2,3,4,6}

print(set_a & set_b & set_c)

# 3a. Dictionaries link 2 strings or numbers together in a key/value pair. Dictionary will be inside curly braces with a colon separating the key and the value. Commas separate the key/value pairs.

# 3b. user:age dictionaries
dict_a = {
    "Steve : 35", "Greg : 28", "Phil : 25"
}
dict_b = {
    "John : 18", "Sam : 40", "Hank : 33"
}

dict_a.update(dict_b)

for k in sorted(dict_a):
        print(k)

# 3c. Removing and adding dictionary entries

dict_c = {
        "Freddy" : "$$$", "Bill" : "$$", "Bob" : "$"
}
del dict_c["Freddy"]
dict_c["Jimmy"] = "$"

print(dict_c)

# 4a. User input replace vowel with *

state = input("What state do you live in? ")
state_upper = state.upper()

state_upper = state_upper.replace("A","*")
state_upper = state_upper.replace("E","*")
state_upper = state_upper.replace("I","*")
state_upper = state_upper.replace("O","*")
state_upper = state_upper.replace("U","*")
state_upper = state_upper.replace("Y","*")
print(state_upper)

# 4b. Reverse string

city = input("What city do you live in? ")
print(city[: : -1])

# 4c. Validate email address

email = input("Enter your email address: ")
at_sign = email.find("@")
domain = email.find(".com")

if at_sign and domain != -1:
        print(f"{email}, seems legit. WELCOME!")
else:
        print(f"{email}, seems a little fishy. Are you sure you entered the information correctly?")

# 4d Obtaining personal info

namee = input("What is your name? ")
age = input("How old are you? ")
citee = input("What city do you live in? ")
phone = input("What is your phone number? ")

print(f"Your name is {namee}, and you are {age} years old. You live in {citee}, and your phone number is {phone}.")


