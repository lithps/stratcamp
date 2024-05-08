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
                key = item[0]
                value = float(item[1])
                NVDA_dict_list.append(value)
            NVDA_dict[key] = NVDA_dict_list
            return(NVDA_dict)

    except FileNotFoundError:
        return "The file path you entered is not found. Please try again."

price_dict()
NVDA_dict = price_dict()

# Loop through the dictionary
for key, values in NVDA_dict.items():
    num_of_items = len(values)
    sum_of_items = sum(values)
average_price = round(sum_of_items / num_of_items, 2)
print(f" The average price of {key} is ${average_price}.")



