class Student:
    def __init__(self, **info):
        if len(info) > 3:
            print(f"too many arguments. {info}")
        elif 1<=len(info)<=3:
            if 'studentName' in info.keys():
                self.studentName = info['studentName']
            if 'studentID' in info.keys():
                self.studentID = info['studentID']
            if 'studentCGPA' in info.keys():
                self.studentCGPA = info['studentCGPA']

            if 'studentName' in info.keys():
                if 'studentID' in info.keys():
                    if 'studentCGPA' in info.keys():
                        print(f'Student name is {self.studentName}, student ID  is {self.studentID} and CGPA is {self.studentCGPA}')
                    else:
                        print(f'Student name is {self.studentName}, student ID  is {self.studentID}')
                elif 'studentCGPA' in info.keys():
                    print(f'Student name is {self.studentName}, CGPA is {self.studentCGPA}')
                else:
                    print(f'Student name is {self.studentName}')
            elif 'studentID' in info.keys():
                    if 'studentCGPA' in info.keys():
                        print(f"Student ID  is {self.studentID} and CGPA is {self.studentCGPA}")
                    else:
                        print(f"Student ID  is {self.studentID}")
            elif 'studentCGPA' in info.keys():
                print(f'CGPA is {self.studentCGPA}')


        else:
            self.studentName = None
            self.studentID = None
            self.studentCGPA = None
            print("A student with empty info has been created.")


s1 = Student()
s2 = Student()
s3 = Student(studentName="A", studentID=7465251)
s3 = Student(studentID=160041014)  # This will throw an  KeyError: 'studentName', fix bugs like this.
s4 = Student(studentID=160041014, studentCGPA=3.98, studentName="B")
