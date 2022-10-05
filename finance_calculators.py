#Compulsory task 1

#imorting math library
import math

#Printing user instructions
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment  - to calculate the amount of interest you'll earn on interest\nbond        - to calculate the amount you'll have to pay on a home loan")
calc_type = input(": ")

#Investment calculator
if calc_type == "Investment" or calc_type =="investment" or calc_type== "INVESTMENT":
    deposit_amount= float(input("How much money are you depositing?: "))
    interest_rate=int(input("What is the interest rate?(Write as a number not percentage): "))
    years= int(input("Number of years years you plan to invest for (write just the number): "))
    interest= input("Do you want to invest on compound or simple interest?\n1.Compund\n2.Simple\n: ")

#nested if statement for the different interest option
    if interest =="1":
        investment_calc = deposit_amount*(1+interest_rate*years)
        print(investment_calc)
#error fixed change 2 to "2"
    elif interest =="2":
        investment_calc = deposit_amount*math.pow((1+interest_rate),years)
        print(investment_calc)

#Bond calculator 
elif calc_type == "Bond" or calc_type== "bond" or  calc_type== "BOND":
    present_value = float(input("What is the present value of the house?: "))
    interest_rate = int(input("What is the interest rate?(Write as a number not percentage): "))
    repay_months = int(input("How many months do you plan to take to repay the bond?: "))
    i = (interest_rate/100)/12
    bond_calc = (i*present_value)/(1-math.pow((1+interest_rate),-repay_months))
    print(bond_calc)

#Error command
else:
    print("Error: The calculation type you've entered is invalid")
