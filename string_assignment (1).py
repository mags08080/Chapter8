# -*- coding: utf-8 -*-
"""string_assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jnXNdLG96GbbhQ-9ATAjl9_A2RbAX3IZ
"""

## create a program that will count the number of times the letter T (uppercase or lowercase) appears in a string
#get a string from user
string = input("Enter a string: ")

#variable to use to hold the count
count = 0

#count the Ts and print the result
for letter in string:
    if letter == "T" or letter == "t":
        count += 1
print("The letter T appears", count, "times in the string")

## create a program that will split date string and display each piece of the date
#create a string with a date
date = '11/11/2023'

#split the date
month, day, year = date.split('/')

#display each piece of the date
print("Month:", month)
print("Day:", day)
print("Year:", year)

## create a program that gets the user's first name, last name, and student ID number. Using this data it genertes a system login user
firstName = input("Enter your first name: ")
lastName = input("Entery your last name: ")
studentID = input("Enter your student ID number: ")

#get the first three letters of the first name. If the name is less than 3 characters, the slice will return the entire first name
firstThreeLetters1 = firstName[:3].lower()
if len(firstName) < 3:
    userName1 = firstName.lower()
else:
    userName1 = firstThreeLetters1

#get first three letters of last name and do the same
firstThreeLetters2 = lastName[:3].lower()
if len(lastName) < 3:
    userName2 = lastName.lower()
else:
    userName2 = firstThreeLetters2

#get last three digits of ID and do the same
lastThreeDigits = studentID[-3:]
if len(studentID) < 3:
    userName3 = studentID.lower()
else:
    userName3 = lastThreeDigits

#return the login name
print("Your user name is:", userName1 + userName2 + userName3)

## create a program to determine whether all of the requirements are met for a valid password
#start by setting boolean variables to false
correct_length = False
has_uppercase = False
has_lowercase = False
has_digit = False

#get user to enter the password
password = input("Enter your password: ")

#begin the validation of password's length
if len(password) >= 7:
    correct_length = True

#test each character and set the appropriate flag when a required character is found
for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True

#print the results
if correct_length and has_uppercase and has_lowercase and has_digit:
    print("True")
else:
    print("False")