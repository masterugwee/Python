#Get user input of how many students and number of subjects.
#We need name and marks of each student and we also have to find the average of each student and compare that.
#Print the list of all students according to their ranks.
#Also student who scored less than 40 is not eligible to be ranked.
#We should print the list of students who failed in any of the subjects.
class Student:
    def __init__(self,students,subjects):
        self.students = students
        self.subjects = subjects
    def AddStudentInfo(self):
        studentdetails = {}
        orderdic = {}
        for i in range(self.students):
            name = input("Enter name of the student")
            ar = []
            passorfail = "PASS"
            print("Enter the marks ")
            for j in range(self.subjects):
                mark = int(input())
                ar.append(mark)
                if(mark<40):
                    passorfail = "FAIL"
            avg = (sum(ar))/self.subjects
            ar.append(passorfail)
            ar.append(avg)
            studentdetails.update({name:ar})
        #ordereddic = sorted(studentdetails.items(), key=lambda e: e[1][-1], reverse= True)
        print("Failed Students")
        for key,value in studentdetails.items():
            if(value[-2] =="FAIL"):
                print(key,value)
        print("Student Rank")
        for key,value in studentdetails.items():
            if(value[-2] =="PASS"):
                orderdic.update({key:value})
        ordereddic = sorted(orderdic.items(), key=lambda e: e[1][-1], reverse=True)
        print(ordereddic)
student = Student(int(input("Enter the number of students")),int(input("Enter the number of subjects")))
student.AddStudentInfo()
