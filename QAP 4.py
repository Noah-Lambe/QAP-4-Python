# Description: A program to enter and calculate insurance policy information for new customers of One Stop Insurance Company.
# Author: Noah Lambe
# Dates: July 15, 2024 - July 18, 2024

# Define required libraries.
from datetime import datetime, timedelta
import datetime
import sys
import time
import FormatValues as fv

# Define program constants.
f = open("Const.dat", "r")

POLICY_NUMBER = int(f.readline().strip())
BASIC_PREMIUM_RATE = float(f.readline().strip())
ADDITIONAL_CAR_DISCOUNT = float(f.readline().strip())
LIABILITY_COVERAGE_RATE = float(f.readline().strip())
GLASS_COVERAGE = float(f.readline().strip())
CAR_LEND_COVERAGE = float(f.readline().strip())
TAX_RATE = float(f.readline().strip())
PROCESSING_FEE = float(f.readline().strip())

f.close()

VALID_PROVINCES = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

# Define program functions.
def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} {bar} {percent}% {suffix}')
    sys.stdout.flush()

def first_day_of_next_month():
    today = datetime.date.today()
    first_next_month = today.replace(day=1) + timedelta(days=32)
    first_next_month = first_next_month.replace(day=1)
    return first_next_month

def format_phone_number(phone):

    phoneNumberStr = f"(" + phone [0:3] + ")" + " " + phone [3:6] + "-" + phone [6:10]

    return phoneNumberStr

# Start main program loop.
while True:

    # Gather and validate user inputs.
    while True:
        print()
        firstName = input("Enter customer's first name: ").capitalize()

        if firstName == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif not firstName.isalpha():
            print()
            print("     Invalid input. Please enter a valid first name.")
        else:
            break

    while True:
        print()
        lastName = input("Enter customer's last name: ").capitalize()

        if lastName == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif not lastName.isalpha():
            print()
            print("     Invalid input. Please enter a valid last name.")
        else:
            break
    
    while True:
        print()
        address = input("Enter customer's address: ").title()

        if address == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        else:
            break
    
    while True:
        print()
        city = input("Enter customer's city: ").title()

        if city == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        else:
            break
    
    while True:
        print()
        province = input("Enter customer's province (XX): ").upper()

        if province == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif province not in VALID_PROVINCES:
            print()
            print("     Invalid input. Please enter a valid province abbreviation.")
        else:
            break

    while True:
        print()
        postalCode = input("Enter customer's postal code (X#X #X#): ").upper().replace(" ", "")

        if postalCode == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif len(postalCode)!= 6:
            print()
            print("     Invalid input. Please enter a valid postal code.")
        else:
            break

    while True:
        print()
        phoneNumber = input("Enter customer's phone number (###-###-####): ").replace("-", "")

        if phoneNumber == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif len(phoneNumber)!= 10:
            print()
            print("     Invalid input. Please enter a valid phone number.")
        else:
            break

    while True:
        print()
        numberOfVehicles = int(input("Enter the number of vehicles being insured: "))

        if numberOfVehicles == "":
            print()
            print("     Invalid input. Field cannot be blank.")
        elif numberOfVehicles <= 0:
            print()
            print("     Invalid input. Number of vehicles must be greater than 0.")
        else:
            break

    while True:
        print()
        extraLiability = input("Would you like to insure extra liability coverage? (Y/N): ").upper()

        if extraLiability!= "Y" and extraLiability!= "N":
            print()
            print("     Invalid input. Please enter either Y or N.")
        else:
            break
    
    while True:
        print()
        glassCoverage = input("Would you like to insure glass coverage? (Y/N): ").upper()

        if glassCoverage!= "Y" and glassCoverage!= "N":
            print()
            print("     Invalid input. Please enter either Y or N.")
        else:
            break

    while True:
        print()
        carLend = input("Would you like to insure car lending coverage? (Y/N): ").upper()

        if carLend!= "Y" and carLend!= "N":
            print()
            print("     Invalid input. Please enter either Y or N.")
        else:
            break
    
    
    downPayment = 0 # Initialize payment options.
    monthlyPayment = 0

    while True:
        print()
        paymentOptions = input("Enter preferred payment option, full, monthly or down payment (F, M, D): ").upper()

        if paymentOptions not in ["F", "M", "D"]:
            print()
            print("     Invalid input. Please enter a valid payment option.")
            continue
        
        while True:
            if paymentOptions == "D":
                
                try:
                    print()
                    downPayment = input("Enter the down payment amount: ")

                    if downPayment == "":
                        print()
                        print("     Invalid input. Field cannot be blank.")
                        continue

                    downPayment = float(downPayment)

                    if downPayment <= 0:
                        print()
                        print("     Invalid input. Down payment amount must be greater than 0.")
                        continue
                    else:
                        break
                except ValueError:
                    print()
                    print("     Invalid input. Enter a valid down payment amount.")
            
            else:
                break

        break

    claims = []

    while True:
        # Input claim details
        while True:
            print()
            claimNumber = input("Enter claim number (#####): ")

            if len(claimNumber)!= 5:
                print()
                print("     Invalid input. Claim number must be 5 characters. (#####).")
            elif not claimNumber.isdigit():
                print()
                print("     Invalid input. Claim number must be 5 digits. (#####).")
            else:
                break

        while True:
            print()
            claimDate = input("Enter claim date (YYYY-MM-DD): ")

            try:
                claimDate = datetime.datetime.strptime(claimDate, "%Y-%m-%d").date()
                break
            except ValueError:
                print()
                print("     Invalid input. Enter a valid claim date (YYYY-MM-DD).")
                continue

        while True:
            print()
            try:
                claimAmount = input("Enter claim amount (0 - 99,999.99): ")

                if claimAmount == "":
                    print()
                    print("     Invalid input. Field cannot be blank.")
                    continue

                claimAmount = float(claimAmount)

                if claimAmount < 0 or claimAmount > 99999.99:
                    print()
                    print("     Invalid input. Claim amount must be between 0 and 99,999.99.")
                else:
                    break
            except ValueError:
                print()
                print("     Invalid input. Claim amount must be a number.")


        claim = {
            'claimNumber': claimNumber,
            'claimDate': fv.FDateS(claimDate),
            'claimAmount': fv.FDollar2(claimAmount)
        }

        claims.append(claim)
        
        print()
        exit_choice = input("Do you want to add another claim? (Y/N): ").upper()
        if exit_choice == 'N':
            break
            
    # Perform required calculations.
    
    if numberOfVehicles > 1:
        discount = ((numberOfVehicles - 1) * BASIC_PREMIUM_RATE) * ADDITIONAL_CAR_DISCOUNT
        premiumCost = numberOfVehicles * BASIC_PREMIUM_RATE - discount
    else:
        premiumCost = numberOfVehicles * BASIC_PREMIUM_RATE

    if extraLiability == "Y":
        extraLiabilityCost = numberOfVehicles * LIABILITY_COVERAGE_RATE
    else:
        extraLiabilityCost = 0
    
    if glassCoverage == "Y":
        glassCoverageCost = numberOfVehicles * GLASS_COVERAGE
    else:
        glassCoverageCost = 0

    if carLend == "Y":
        carLendCost = numberOfVehicles * CAR_LEND_COVERAGE
    else:
        carLendCost = 0

    totalExtraCost = extraLiabilityCost + glassCoverageCost + carLendCost
    totalInsurancePremium = premiumCost + totalExtraCost
    taxAmount = totalInsurancePremium * TAX_RATE
    totalCost = totalInsurancePremium + taxAmount

    while True:
        if downPayment > totalCost:
            print()
            print("     Policy Calculation Failed.")
            print("     Invalid input. Down payment cannot exceed total cost.")
            
            try:
                print()
                downPayment = input("Enter the down payment amount: ")

                if downPayment == "":
                    print()
                    print("     Invalid input. Field cannot be blank.")
                    continue

                downPayment = float(downPayment)

                if downPayment <= 0:
                    print()
                    print("     Invalid input. Down payment amount must be greater than 0.")
                    continue
                else:
                    break

            except ValueError:
                print()
                print("     Invalid input. Enter a valid down payment amount.")
        else:
            break

    if paymentOptions == "M":
        monthlyPayment = (PROCESSING_FEE + totalCost) / 8
    elif paymentOptions == "D":
        monthlyPayment = (PROCESSING_FEE + (totalCost - downPayment)) / 8

    invoiceDate = datetime.date.today()
    firstPaymentDate = first_day_of_next_month()

    # Format Outputs.
    invoiceDateDSP = fv.FDateS(invoiceDate)
    firstPaymentDateDSP = fv.FDateS(firstPaymentDate)
    fullNameDSP = f"{firstName} {lastName}"
    phoneNumberDSP = format_phone_number(phoneNumber)

    if paymentOptions == "D":
        paymentOptionsDSP = "Down Payment"
    elif paymentOptions == "F":
        paymentOptionsDSP = "Full Payment"
    elif paymentOptions == "M":
        paymentOptionsDSP = "Monthly Payment"

    if extraLiability == "Y":
        extraLiabilityDSP = "Yes"
    else:
        extraLiabilityDSP = "No"

    if glassCoverage == "Y":
        glassCoverageDSP = "Yes"
    else:
        glassCoverageDSP = "No"

    if carLend == "Y":
        carLendDSP = "Yes"
    else:
        carLendDSP = "No"
    
    premiumCostDSP = fv.FDollar2(premiumCost)
    extraLiabilityCostDSP = fv.FDollar2(extraLiabilityCost)
    glassCoverageCostDSP = fv.FDollar2(glassCoverageCost)
    carLendCostDSP = fv.FDollar2(carLendCost)
    totalExtraCostDSP = fv.FDollar2(totalExtraCost)
    totalInsurancePremiumDSP = fv.FDollar2(totalInsurancePremium)
    taxAmountDSP = fv.FDollar2(taxAmount)
    totalCostDSP = fv.FDollar2(totalCost)
    downPaymentDSP = fv.FDollar2(downPayment)
    monthlyPaymentDSP = fv.FDollar2(monthlyPayment)

    # Display outputs.
    print()
    print(f"----------------------------------------------------------------------")
    print(f"                      One Stop Insurance Company                      ")
    print(f"                           Date: {invoiceDateDSP:>10s}                ")
    print(f"                         Policy Number: {POLICY_NUMBER}")
    print(f"----------------------------------------------------------------------")
    print()
    print(f"Customer: {fullNameDSP:<20s}  Address: {address:<29s}")
    print(f"Phone: {phoneNumberDSP:<14s}                    {city:<25s}, {province:<2s}")
    print(f"                                         {postalCode:<6s}")
    print()
    print(f"Number of Vehicles: {numberOfVehicles:<3d}                  Extra Liability Coverage: {extraLiabilityDSP:<3s}")
    print(f"Payment option: {paymentOptionsDSP:<15s}          Glass Repair Coverage:    {glassCoverageDSP:<3s}")
    print(f"Date of first payment: {firstPaymentDateDSP:<10s}        Car Lending Coverage:     {carLendDSP:<3s}")
    print()
    print(f"----------------------------------------------------------------------")
    print()
    print(f"Premium Cost:                                               {premiumCostDSP:>10s}")
    print(f"Down Payment:                                               {downPaymentDSP:>10s}")
    print(f"Monthly Payment:                                            {monthlyPaymentDSP:>10s}")
    print(f"                                                           -----------")
    print(f"Extra Liability Cost:                                       {extraLiabilityCostDSP:>10s}")
    print(f"Glass Coverage Cost:                                        {glassCoverageCostDSP:>10s}")
    print(f"Car Lending Coverage Cost:                                  {carLendCostDSP:>10s}")
    print(f"                                                           -----------")
    print(f"Total Extra Cost:                                           {totalExtraCostDSP:>10s}")
    print(f"Total Insurance Premium:                                    {totalInsurancePremiumDSP:>10s}")
    print(f"Tax Amount:                                                 {taxAmountDSP:>10s}")
    print(f"                                                           -----------")
    print(f"Total Cost:                                                 {totalCostDSP:>10s}")
    print(f"----------------------------------------------------------------------")
    print()
    print(f"               Claim #        Claim Date        Amount                ")
    print(f"              -----------------------------------------")
    print()

    for claim in claims:
        print(f"                {claim['claimNumber']:>5s}         {claim['claimDate']:<10s}     {claim['claimAmount']:>10s}")

    print()
    print(f"----------------------------------------------------------------------")

    # Save policy data to Customers.dat.
    f = open("Customers.dat", "a")

    f.write(f"{POLICY_NUMBER}, ")
    f.write(f"{firstName}, ")
    f.write(f"{lastName}, ")
    f.write(f"{address}, ")
    f.write(f"{city}, ")
    f.write(f"{province}, ")
    f.write(f"{postalCode}, ")
    f.write(f"{phoneNumber}, ")
    f.write(f"{numberOfVehicles}, ")
    f.write(f"{extraLiability}, ")
    f.write(f"{glassCoverage}, ")
    f.write(f"{carLend}, ")
    f.write(f"{paymentOptions}, ")
    f.write(f"{invoiceDate}, ")
    f.write(f"{totalInsurancePremium:.2f}\n")

    f.close()
    
    # Generate and display progress bar.
    print()
    TotalIterations = 30
    Message = "Saving Policy Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)
        progress_bar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()
 
    print()
    print(f"Policy information for {firstName} {lastName} has been successfully saved to Customers.dat ...")
    print()

    POLICY_NUMBER += 1

    print()
    Continue = input("Do you want to create another policy? (Y/N): ").upper()
    if Continue == "N":
        break

# Concluding program.
print()
print("Have a great day!")
print()

# Save the current data to Const.dat.
f = open(f"Const.dat", "w")
f.write(f"{POLICY_NUMBER}\n")
f.write(f"{BASIC_PREMIUM_RATE}\n")
f.write(f"{ADDITIONAL_CAR_DISCOUNT}\n")
f.write(f"{LIABILITY_COVERAGE_RATE}\n")
f.write(f"{GLASS_COVERAGE}\n")
f.write(f"{CAR_LEND_COVERAGE}\n")
f.write(f"{TAX_RATE}\n")
f.write(f"{PROCESSING_FEE}\n")
f.close()