import math

#Request input(pick between bond or investment calculator) from the user
#expected input values "investment" or "bond"
calculator_type = input("Choose either \'investment\' for \'bond\' from the menu below to proceed: \n"
                      "\n\'investment\' - to calculate the amount of interest you will earn on your investment \n"
                       "\'bond\' - to calculate the amount of you will have to pay on a home loan \n"
                         "\nYour input: ")

#To get rid of the issues that might come because some users might capitalise their selection
#some not....we going to make the input value uniform here.
#by converting the input into lower case
calculator_type = calculator_type.lower()
#print(calculator_type)

#Based on the user input(calculator_type) we will request for more inputs
#and we will output the result of the calculation
#We will show error message if invalid selection is made
if calculator_type == "investment":
    #If user selects "investment" calculator
    #request the following inputs
    deposit_amt = float(input("What is that amount ot money your want to deposit: R "))
    numberOfInvst_years = int(input("For how many years are you planing to invest: "))
    interest_rate = float(input("What is the interest rate(Don't include the \"%\"): "))
    interest = input("Select interest type: \'Simple\' or \'Compound\' \n"
                     "Your selection: ")

    #Simple and compound interest formula details
    # simple interest formula ~ A = P(1+r*t)
    # compound interest formula ~ A = P*(1+r)^t
    #"r" is the interest entered above divided by 100
    #"P" is the amount that user deposits
    #"t" is the number of years that the money is being invested
    #"A" is the total amount once the interest has been applied

    #We will make the selection uniform by making the imput all lower case
    interest = interest.lower()

    #investment calculation based on the user inputs
    if interest == "simple":
        #Calculation for simple interest
        spTotal_amount = round(deposit_amt * (1 + (interest_rate / 100) * numberOfInvst_years), 2)
        print("Your total amount is: R", str(spTotal_amount), " in", numberOfInvst_years, "years.")

    elif interest == "compound":
        #Calculation for compund interest
        compTotal_amount = round(deposit_amt * math.pow((1 + (interest_rate / 100)), numberOfInvst_years), 2)
        print("Your total amount is: R", str(compTotal_amount), " in", numberOfInvst_years, "years.")
    else:
        # If user inputs invalid selection for interest
        # show error message
        print("Invalid selection: Please select \'simple\' or \'compound\'.")

elif calculator_type == "bond":
    # If user selected "bond" calculator
    # request the following inputs
    house_value = float(input("What is the present value of the house: "))
    interestRate_yearly = float(input("What is the interest rate(Don't include the \"%\"): "))
    repayment_numOfMonths = int(input("How many months is the repayment: "))

    #Bond repayment calculations
    #Bond repayment formula  =  repayment = x =(i.P) / (1 - (1 + i)^(-n))
    #"P" is the present value of the house
    #"i" is the monthly interest rate. calculated by diving the annual interest rate by 12
    #"n" is the nummber of months over which the bond will be repaid

    #Calculating how much money the user will have to repay each month
    #printing that output
    interestRate_monthly = (interestRate_yearly / 12) / 100
    monthly_repayment = round((interestRate_monthly * house_value) / (1 - (1 + interestRate_monthly) ** (-1 * repayment_numOfMonths)), 2)
    print("The monthly repayment is:", str(monthly_repayment), "for", str(repayment_numOfMonths), "months.")
else:
    # If user inputs invalid selection for calculator type
    # show error message
    print("Invalid selection: Please make sure you selected \'investment\' or \'bond\'.")