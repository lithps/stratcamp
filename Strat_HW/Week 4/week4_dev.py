# 1a.
#define function that varies filepath
def verify_path(fname):
        # try to use file path (see exception if error)
        try:
            # open and read the file
            with open (fname, "r") as file:
                    contents = file.read()
            # variable that represents no. of characters in file
            char_count = len(contents)
            # statement returns true if there is at least 1 character in the file
            if char_count >= 1:
                    return True
            # statement returns false if file is blank
            else:
                    return False
        # if filepath/name entered is not valid print the string below
        except FileNotFoundError:
              return f"The filepath/name {fname} cannot be found. Try entering the filepath/name again."
# create a variable for the user's filepath and filename
user_fname = input("What is the filepath/filename? ")
# run the input from the user through the verify_path function, make the result a variable     
result = verify_path(user_fname)
# create statement if false is returned from verify_path function
if result is False:
        # open file and write
        with open(user_fname, "w") as file:
                # write the string to the file
                file.write("This file is quite possibly empty :(")
elif result is True:
    # name of new file
    new_file = "new_file.txt"
    #open and write on new file
    with open(new_file, "w") as file:
           file.write("This is a new file.")
else:
      print(result)

#3 Finance App

# define function
def price_dict():
    # import csv module
    import csv
    # file path stored as variable
    fname = "/home/josh/stratcamp-1/Strat_HW/Week 4/week4_stock_data.csv"
    NVDA_dict = {}
    NVDA_dict_list = []
    NVDA_list = []
    try:
        # open file
        with open(fname,"r") as file:
            # run file variable through CSV reader. Store this as a variable
            csv_reader = csv.reader(file)
            # skip the header row
            next(csv_reader)
            # use for loop to read this row by row
            for row in csv_reader:
                # consolidate each row to a master list
                NVDA_list.append(row)
            # loop through each item in list   
            for item in NVDA_list:
                # explain index of the key
                key = item[0]
                # explain index of the value
                value = float(item[1])
                # append values to one large list
                NVDA_dict_list.append(value)
            # make the list containing prices the value that corresponds to the key
            NVDA_dict[key] = NVDA_dict_list
            # return the dict
            return(NVDA_dict)
    # exception with error msg if incorrect file path
    except FileNotFoundError:
        return "The file path you entered is not found. Please try again."
# call function
price_dict()
# assign variable to dictionary returned by function so dictionary can be interacted with
NVDA_dict = price_dict()

# Loop through the dictionary
for key, values in NVDA_dict.items():
    # count no. of values
    num_of_items = len(values)
    # sum the values
    sum_of_items = sum(values)
# find the average and round to 2 decimals
average_price = round(sum_of_items / num_of_items, 2)
# print result
print(f" The average price of {key} is ${average_price}.")



