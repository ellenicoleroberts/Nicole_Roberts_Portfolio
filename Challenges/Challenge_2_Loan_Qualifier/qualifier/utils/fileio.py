# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
from pathlib import Path
import csv
import sys
import questionary
import os.path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skips the CSV Header
        next(csvreader)

        # Reads the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    
    """
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    # If user does not qualify for any loans, quits the application.
    if len(qualifying_loans) == 0:
        sys.exit("Sorry, you do not qualify for any loans. Goodbye.")

    # Asks user if they would like to save their list of qualfied loans.    
    proceed = questionary.confirm("Would you like to save your list of qualified loans? Please enter yes or no.").ask()
    
    # Gets the output file path from the user.
    if proceed: 
        output_file_path = questionary.text("Please enter an output file path (.csv) to save your list of qualifying loans.").ask()
        name, extension = os.path.splitext(output_file_path)
        if extension == ".csv":
            csvpath = Path(output_file_path)  #Creates a Path to a new CSV file
        else:
            output_file_path = questionary.text("Incorrect file format. Please enter a .csv file path to save your list of qualifying loans.").ask()
            name, extension = os.path.splitext(output_file_path)
            if extension == ".csv":
                csvpath = Path(output_file_path)  #Creates a Path to a new CSV file
            else:
                sys.exit("You have failed to input the correct file format so your list of loans has not been saved. Goodbye.")
    else: 
        sys.exit("Thank you for using the Loan Qualifier Application. Goodbye.")

    # Opens the output CSV file path using `with open` and writes the 'qualifying_loans' list to a .csv file
    with open(csvpath, 'w', newline='') as csvfile:  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        for row in qualifying_loans:
            csvwriter.writerow(row)
   
    print(f"Your list of loans you qualify for has been saved to {output_file_path}.")