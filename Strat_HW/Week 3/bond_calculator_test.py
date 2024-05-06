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
    final_sum = round(final_sum, 2)
    return final_sum
# print the final result
print(f"PV = ${bond_pricer()}")