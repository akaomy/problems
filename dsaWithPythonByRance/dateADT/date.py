class Date:

    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."

        temp = 0
        if month < 3:
            temp = -1
        self._julianDay = day - 32075 
        + (1461 * (year + 4800 + temp) // 4) 
        + (367 * (month - 2 - temp * 12) // 12)
        - (3 * ((year + 4900 + temp) // 100) // 4)

        # extracts the appropriate Gregorian date component
        def month(self):
            return (self._toGregorian())[0] # return M from (M, d, y)

        def day(self):
            return (self._toGregorian())[1] # return M from (m, D, y)

        def year(self):
            return (self._toGregorian())[2] # return M from (m, d, Y)

    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day 
        + year + year // 4 - year // 100 + year // 400) % 7

    # returns string in Gregorian format
    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)
    
    # logically compares two dates
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay
    
    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    # todo other methods
    # todo
    # tests the supplied Gregorian
    # date components and returns the appropriate boolean value.
    def _isValidGregorian(self):
        pass

    # returns Gregorian date as a tuple: (month, day, year)
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year