import zope.interface 

class Date(zope.interface.Interface):

    # Creates a new Date instance initialized to the given 
    # Georgian date which must be valid. Year 1 BC and earlier are indicated by 
    # negative year components.
    def Date(month, day, year):
        pass

    # Returns the Gregorian day number of this date.
    def day():
        pass

    # Returns the Gregorian month number of this date.
    def month():
        pass

    # Returns the Gregorian year of this date.
    def year():
        pass

    # Returns the Gregorian month name of this date.
    def monthName():
        pass

    # Returns the day of the week as a number between 0 and 6 with
    # 0 representing Monday and 6 representing Sunday.
    def dayOfWeek():
        pass

    # Returns the number of days as a positive integer be-
    # tween this date and the otherDate.
    def numDays(otherDate):
        pass

    # Determines if this date falls in a leap year and returns the
    # appropriate boolean value.
    def isLeapYear():
        pass

    # Advances the date by the given number of days. The date
    # is incremented if days is positive and decremented if days is negative. The
    # date is capped to November 24, 4714 BC, if necessary.
    def advanceBy( days ):
        pass

    # Compares this date to the otherDate to deter-
    # mine their logical ordering. This comparison can be done using any of the
    # logical operators <, <=, >, >=, ==, !=.
    def comparable ( otherDate ):
        pass

    # Returns a string representing the Gregorian date in the format
    # mm/dd/yyyy. Implemented as the Python operator that is automatically called
    # via the str() constructor.
    def toString ():
        pass



print(type(Date))
print(Date.__module__)
print(Date.__name__)