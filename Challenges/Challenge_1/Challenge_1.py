# coding: utf-8
import csv
from pathlib import Path

annual_discount_rate = .20

print("\nPart 1: Automate the Calculations.\n")

loan_costs = [500, 600, 200, 1000, 450] #list of loans

total_number_of_loans = len(loan_costs) #how many loans are in the list of loans
print(f"The total number of loans is {total_number_of_loans}.")

sum_of_all_loans = sum(loan_costs) #the total value of all of the loans in the list
print(f"The total value of all of the loans is ${sum_of_all_loans}.")

average_loan_amount = sum_of_all_loans / total_number_of_loans #the average value of the loans in the list
print(f"The average loan price is ${average_loan_amount}.")

print("\nPart 2: Analyze Loan Data.\n")

loan = { #a dictionary containing information of a specific loan
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value") #the future value of this loan
remaining_months = loan.get("remaining_months") #how many months are remaining until payment is due for this loan

print(f"The future value of the loan is ${future_value}.")
print(f"There are {remaining_months} months remaining on this loan.")

present_value_of_loan1 = future_value / (1 + (annual_discount_rate/12))**remaining_months #the present value of this loan

if present_value_of_loan1 >= loan["loan_price"]: #conditional statement that determines whether or not this loan is worth buying
    print(f"The present value of this loan is ${round(present_value_of_loan1, 2)} and is worth at least the cost to buy it.")
else:
    print(f"The present value of this loan is ${round(present_value_of_loan1), 2}. It is too expensive and not worth the price.")

print("\nPart 3: Perform Financial Calculations.\n")

def present_value(future_value, remaining_months, annual_discount_rate): #a function that calculates a loan's present value
    present_value = future_value / (1 + (annual_discount_rate/12))**remaining_months
    return present_value

new_loan = { #a dictionary containing information of a specific loan
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

present_value_of_loan2 = present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate) #using the function
#defined above, calculates the present value of the specific loan

print(f"The present value of the loan is ${round(present_value_of_loan2, 2)}.")

print("\nPart 4: Conditionally filter lists of loans.\n")

loans = [  #a list containing information for a number of loans
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = [] #an empty list that will be filled below depending on loan prices

for loan in loans: #a for loop that filters the "loans" list according to price; loans <= $500 are added to the "inexpensive_loans" list.
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print("Here is the list of inexpensive loans:\n")
print(inexpensive_loans)

print("\nPart 5: Save the results.\n")

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"] #a header that will be printed to a CSV file created below

output_path = Path("inexpensive_loans.csv") #creates a Path object, "inexpensive_loans.csv"

with open(output_path, 'w', newline='') as csvfile: #using the assigned Path object, opens the new "inexpensive_loans.csv" file in write mode
    csvwriter = csv.writer(csvfile) #creates a `csvwriter` using the `CSV` library to write data to the "inexpensive_loans.csv" file
    csvwriter.writerow(header) #writes the header to the "inexpensive_loans.csv" file; will be the first row in the CSV file
    for loan in inexpensive_loans: #a for loop that iterates through every loan in the inexpensive_loans list
        csvwriter.writerow(loan.values()) #writes each loan's information to its own row in the "inexpensive_loans.csv" file

print("The list of inexpensive loans has been written to inexpensive_loans.csv.")



