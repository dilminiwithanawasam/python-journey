class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def showDetails(self):
        print("University Name:",self.uni_name)
class Course(University):
    def __init__(self,uni_name,course_name,course_code):
        University.__init__(self,uni_name)
        self.course_name=course_name
        self.course_code=course_code
    def showCourseDetails(self):
        print("Course Name:",self.course_name)
        print("Course Code:",self.course_code)
class Branch(University):
    def __init__(self,uni_name,branch_name):
        University.__init__(self,uni_name)
        self.branch_name=branch_name
    def showDetails(self):
        super().showDetails()
        print("Branch Name:",self.branch_name)
class Student(Course,Branch):
    def __init__(self,uni_name,course_name,course_code,branch_name,student_name,student_id):
        Course.__init__(self,uni_name,course_name,course_code)
        Branch.__init__(self,uni_name,branch_name)
        self.student_name=student_name
        self.student_id=student_id
    def showDetails(self):
        super().showDetails()
        print("Student Name:",self.student_name)
        print("Student ID:",self.student_id)
class Faculty(Branch):
    def __init__(self,uni_name,branch_name,faculty_name,faculty_id):
        Branch.__init__(self,uni_name,branch_name)
        self.faculty_name=faculty_name
        self.faculty_id=faculty_id
    def showDetails(self):
        super().showDetails()
        print("Faculty Name:",self.faculty_name)
        print("Faculty ID:",self.faculty_id )
student1=Student("ABC University","Computer Science","CS101","Main Branch","John Doe","S12345")
student1.showDetails()