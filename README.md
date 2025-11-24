# Assignment_8-Tuples-and-Sets
This program was made for Assignment 8 to practice using tuples and sets in Python.

The purpose of the program is to analyze a Loans dataset and find the top two most common loan reasons for each age group.

The program reads a CSV file that contains customer information, including age and loan intent.

It detects the correct age column and loan reason column automatically.

It uses a set to collect all unique age ranges from the dataset.

It counts how many times each loan reason appears for every age group.

For each age range, it picks the top two most common loan reasons.

The program stores each final result in a tuple formatted like:

(age_range, top_reason_1, top_reason_2)

After analyzing all data, the program writes a new CSV file that contains all of the tuples.

To run the program:

Run the Python file in the terminal.

Enter the full path to your loans CSV file when prompted.

A new results file ending with “_top_reasons_by_age.csv” will be created automatically.

This assignment uses:

Tuples

Sets

Loops

The built-in csv module

No external libraries like pandas
