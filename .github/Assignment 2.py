#Programmer: Victoria
#Course: CS701/GB-731, Dr. Rajeev
#Date: 10/4/21
#Programming Assignment: 2
#Program Inputs: Month (1-12) and year
#Program Outputs: Number of days in the month

#Program asks user to input month and year and defines variables
month = int(input("Input the month (1-12): "))
year = int(input("Input the year: "))

leapYear = False

#Program calculates if the year is a leap year.
if year % 4 == 0:
    leapYear = True

#Program calculates how many days the year has and prints it.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("This month has 31 days.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("This month has 30 days.")
elif month == 2 and leapYear:
    print("This month has 29 days.")
elif month == 2 and not leapYear:
    print("This month has 28 days.")
else:
    print("Invalid month.")