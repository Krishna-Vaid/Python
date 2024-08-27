#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      krish
#
# Created:     14-07-2024
# Copyright:   (c) krish 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Fixed Deposit Calculator For SBI Bank

#Asking age of customer
while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
        break
    except ValueError:
        print("Please enter a valid age.")


# Asking principal amount from user
while True:
        try:
            principal_amount = int(input("Enter the amount of F.D to be done: "))
            print("Principal amount to be invested:", principal_amount, "Rupees Only")
            print(principal_amount)
            break
        except ValueError:
            print("Please enter a valid number.")

# Duration OF FD using input from user
time = input("F.D to be done for days or years : ").lower()
duration = ""
days = 0
years = 0

# Deciding days or years using if-else statements
while True:
        time = input("F.D to be done for days or years: ").lower()
        if time == "days":
            while True:
                try:
                    days = int(input("Enter number of days: "))
                    if 7 <= days <= 3650:
                        print("Duration of F.D:", days, "Days")
                        print( days)
                        break
                    else:
                        print("Enter valid number of days.")
                        break
                        
            
                except ValueError:
                    print("Please enter a valid number of days.")
        elif time == "years":
            while True:
                try:
                    years = float(input("Enter number of years: "))
                    if 0 < years <= 10:
                        print("Duration of F.D:", years, "Years")
                        print(years, years, time)
                        break
                    else:
                        print("Number of years cannot exceed 10.")
                        
                except ValueError:
                    print("Please enter a valid number of years.")
                    
        else:
            print("Enter a valid input (days or years).")
            break

# Detecting the interest rate according to the duration and age and amount
if age < 60 and principal_amount <30000000 :
    if time == "days" :
        if days >= 7 and days < 46 :
            interest = 3.50
        elif days >= 46 and days < 180 :
            interest = 5.50
        elif days >= 180 and days < 211 :
            interest = 6.25
        elif days >= 211 and days < 365 :
            interest = 6.50
        elif days >= 365 and days < 730 :
            interest = 6.80
        elif days >= 730 and days < 1095 :
            interest = 7.00
        elif days >= 1095 and days < 1825 :
            interest = 6.75
        else :
            interest = 6.50
        print("Interest for this duration will be", interest, "%")
    else :
        if years >= 1 and years < 2 :
            interest = 6.80
        elif years >= 2 and years < 3 :
            interest = 7.00
        elif years >= 3 and years < 5 :
            interest = 6.75
        else :
            interest = 6.50
        print("Interest for this duration will be", interest, "%")
elif age >= 60 and principal_amount < 30000000 :
    if time == "days" :
        if days >= 7 and days < 46 :
            interest = 4.00
        elif days >= 46 and days < 180 :
            interest = 6.00
        elif days >= 180 and days < 211 :
            interest = 6.75
        elif days >= 211 and days < 365 :
            interest = 7.00
        elif days >= 365 and days < 730 :
            interest = 7.30
        elif days >= 730 and days < 1095 :
            interest = 7.50
        elif days >= 1095 and days < 1825 :
            interest = 7.25
        else :
            interest = 7.50
        print("Interest for this duration will be", interest, "%")
    else :
        if years >= 1 and years < 2 :
            interest = 7.30
        elif years >= 2 and years < 3 :
            interest = 7.50
        elif years >= 3 and years < 5 :
            interest = 7.25
        else:
            interest = 7.50
        print("Interest for this duration will be", interest, "%")
elif age < 60 and principal_amount >= 30000000 :
    if time == "days" :
        if days >= 7 and days < 46 :
            interest = 5.25
        elif days >= 46 and days < 180 :
            interest = 6.25
        elif days >= 180 and days < 211 :
            interest = 6.60
        elif days >= 211 and days < 365 :
            interest = 6.75
        elif days >= 365 and days < 730 :
            interest = 7.00
        elif days >= 730 and days < 1095 :
            interest = 7.00
        elif days >= 1095 and days < 1825 :
            interest = 6.50
        else :
            interest = 6.25
        print("Interest for this duration will be", interest, "%")
    else :
        if years >= 1 and years < 2 :
            interest = 7.00
        elif years >= 2 and years < 3 :
            interest = 7.00
        elif years >= 3 and years < 5 :
            interest = 6.50
        else :
            interest = 6.25
        print("Interest for this duration will be", interest, "%")
else:
    if time == "days" :
        if days >= 7 and days < 46 :
            interest = 5.75
        elif days >= 46 and days < 180 :
            interest = 6.75
        elif days >= 180 and days < 211 :
            interest = 7.10
        elif days >= 211 and days < 365 :
            interest = 7.25
        elif days >= 365 and days < 730 :
            interest = 7.50
        elif days >= 730 and days < 1095 :
            interest = 7.50
        elif days >= 1095 and days < 1825 :
            interest = 7.00
        else :
            interest = 6.75
        print("Interest for this duration will be", interest, "%")
    else :
        if years >= 1 and years < 2 :
            interest = 7.50
        elif years >= 2 and years < 3 :
            interest = 7.50
        elif years >= 3 and years < 5 :
            interest = 7.00
        else :
            interest = 6.75
        print("Interest for this duration will be", interest, "%")



# Printing all the details
print("All details are -")
print("Principal amount to be invested :", principal_amount, "Rupees Only")
if time == "days" :
    print("Duration of F.D :", days, "Days")
else:
    print("Duration of F.D :", years, "Years")
print("Age :", age, "Years")
print("Interest rate :", interest, "%")

# Calculating the return value and total value using mathematical formulas
amount= principal_amount*(1+interest/100)**duration
interest_amount = amount-principal_amount
print("Invested Amount :", principal_amount)
print("Return on F.D :", interest_amount)
print("Total Value :", amount)
