from student_file_reader_ADT import StudentFileReader

FILE_NAME = "students.txt"

def main():
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    student_list = reader.fetchAll()
    reader.close()

    # Sort the list by id number. Each object is passed to the lambda
    # expression which returns the idNum field of the object.
    studentList.sort( key = lambda rec: rec.idNum )

    # Print the student report.
    printReport( studentList )

def printReport(lst):
    classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")

    print( "LIST OF STUDENTS".center(50) )
    print( "" )
    print( "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA' ) )
    print( "%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))

    for record in lst:
        print( "%5d %-25s %-10s %4.2f" % \
        (record.idNum, \
        record.lastName + ', ' + record.firstName,
        classNames[record.classCode], record.gpa) )

    print( "-" * 50 )
    print( "Number of students: ", len(lst))

class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0

main()