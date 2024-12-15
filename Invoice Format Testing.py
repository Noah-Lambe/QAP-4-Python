from datetime import datetime, timedelta
import sys
import time
import FormatValues as fv

POLICY_NUMBER = 1944


def first_day_of_next_month():
    today = datetime.today()
    first_next_month = today.replace(day=1) + timedelta(days=32)
    first_next_month = first_next_month.replace(day=1)
    return first_next_month

downPayment = 0
monthlyPayment = 300.00

invoiceDateDSP = "2024-07-16"
fullNameDSP = "John Doe"
address = "123 Maple Street"
phoneNumberDSP = "555-123-4567"
city = "Sampletown"
province = "ON"
postalCode = "A1B2C3"
numberOfVehicles = 2
extraLiability = 'Y'
glassCoverage = 'N'
carLend = 'Y'
premiumCost = 12500.00
extraLiabilityCost = 100.00
glassCoverageCost = 0.00
carLendCost = 50.00
totalExtraCost = extraLiabilityCost + glassCoverageCost + carLendCost
totalInsurancePremium = premiumCost + totalExtraCost
taxAmount = totalInsurancePremium * 0.13
totalCost = totalInsurancePremium + taxAmount
paymentOptionsDSP = "Monthly Payment"
firstPaymentDate = first_day_of_next_month()

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
firstPaymentDateDSP = fv.FDateS(firstPaymentDate)

# claims = []

# while True:
#     # Input claim details
#     claimNumber = input("Enter claim number: ")
#     claimDate = input("Enter claim date (YYYY-MM-DD): ")
#     claimAmount = float(input("Enter claim amount: "))

#     claim = {
#         'claimNumber': claimNumber,
#         'claimDate': claimDate,
#         'claimAmount': claimAmount
#     }

#     claims.append(claim)

#     exit_choice = input("Do you want to add another claim? (Y/N): ").upper()
#     if exit_choice == 'N':
#         break


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

# f = open ("Claims.dat", "r")

# for ClaimRecord in f:

#     ClaimList = ClaimRecord.split(",")

#     ClaimNumber = ClaimList[0].strip()
#     ClaimDate = ClaimList[13].strip()
#     Amount = float(ClaimList[14].strip())

#     AmountDSP = fv.FDollar2(Amount)

#     print(f"                {ClaimNumber:>4s}          {ClaimDate:<10s}     {AmountDSP:>10s}")

# f.close()

# for i in range(len(claims)):
#     claim_number, claim_date, claim_amount = claims[i]
#     print(f"{claimNumber} {claimDate} {claimAmount:.2f}")

# for claim in claims:
#     print(f"              {claim['claimNumber']:>5s}           {claim['claimDate']:<10s}     {claim['claimAmount']:>10.2f}")



# currentDate = datetime.today()

# desiredMonth = currentDate.month + 2

# if desiredMonth > 12:
#     desiredMonth -= 12

# print(f"{desiredMonth}")

#     # Read claim data from Claims.dat and display previous claims.
#     # f = open ("Claims.dat", "r")

#     # for ClaimRecord in f:

#     #     ClaimList = ClaimRecord.split(",")

#     #     ClaimNumber = ClaimList[0].strip()
#     #     ClaimDate = ClaimList[13].strip()
#     #     Amount = float(ClaimList[14].strip())

#     #     AmountDSP = fv.FDollar2(Amount)

#     #     print(f"                {ClaimNumber:>4s}          {ClaimDate:<10s}     {AmountDSP:>10s}")

#     # f.close()