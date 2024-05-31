#This code is written to help identify whether a year is or isn't a leap year based on specific calculations
while True:

    year = int(input("Enter a year: "))


    if int(year%100==0 and int(year%400==0)):
        print(year, "was a leap year!")
    elif int(year%4!=0):
        print(year, "was not a leap year as it's not divisible by 4.")
    elif int(year%100==0) and int(year%400!=0):
        print(year, "was not a leap year as it's not divisible by 400.")
    else:
        print(year, "was a leap year!")