class StudentFileReader:

    # creates a student reader instance for extracting student records from the given file
    # type and format of the file is dependent on the specific implementation
    def StudentFileReader(filename):
        pass

    #  opens connection to the input source and prepares it for extracting student records.
    # if a connection cannot be opened, an exception is raised.
    def open():
        pass

    # Closes the connection to the input source. If the connection is not currently open, an exception is raised.
    def close():
        pass

    # extracts the next student record from the input source and returns a reference to a storage object containing the data.
    # None is returned when there are no additional records to be extracted.
    # An exception is raised if the connection to the input source was previously closed.
    def fetchRecord():
        pass

    # The same as fetchRecords(), but extracts all student records (or those remaining) from the input source and returns then in a Python list.
    def fetchAll():
        pass


class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0