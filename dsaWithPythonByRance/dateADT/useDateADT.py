'''The dates are extracted from standard input and examined.
Those dates that indicate the individual is at least 21 years of age
based on a target date are printed to standard output.
The user is continuously
prompted to enter a birth date until zero is entered for the month.'''

from dateADT import Date

def main():
    bornBefore = Date(6, 1, 1988)
    bag = Bag()

    date = promptAndExtractDate()
    while date is not None:
        bag.add(date)
        #  iterate over the bag and check the age
        for date in bag:
            if bornBefore >= date:
                print("Is at least 21 years of age: ", date)
            date = promptAndExtractDate()
    
   

    def promptAndExtractDate():
        print("Enter a birth date")
        month = int(input("month (0 to quit)"))
        if month == 0:
            return None
        else:
            day = int(input("date: "))
            year = int(input("year: "))
            return Date(month, day, year)

main()
