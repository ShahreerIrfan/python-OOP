class Student:
    def __init__(self,name,id,current_class):
        self.name = name
        self.id = id
        self.current_class = current_class
        
    def __repr__(self):
        return f'Student name is {self.name} Student Id is {self.id} Current class is {self.current_class}'
    
class Teacher:
    def __init__(self,name,id,subject):
        self.name = name
        self.id = id
        self.subject =  subject
    def __repr__(self) -> str:
        return f'Teacher name is {self.name} Teacher ID is {self.id} Teacher subject is {self.subject}'
    
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def addTeacher(self,name,subject):
        id = len(self.teachers)+100
        teacher = Teacher(name,id,subject)
        self.teachers.append(teacher)
        
    def enroll(self,name,fee):
        if fee<6500:
            return f'No enough fee'
        id = len(self.students)+102
        student = Student(name,id,'C')
        self.students.append(student)
        
        return f'Student enrolled name {name} with id {id} extrea money given {fee-6500}'
    def __repr__(self) -> str:
        print('Welcome to our school')
        print('----Our Teachers-----')
        for teacher in self.teachers:
            print(teacher)
        print('----Our students----')
        for student in self.students:
            print(student)
        return f'All done for now'
        
           
    
    
school = School('Primary School')
school.addTeacher('Babu','Math')
school.addTeacher('Shafi','Algo')
school.addTeacher('Ashraf','DLD')
school.addTeacher('Kotha','ISD')
school.enroll('Irfan',6501)
school.enroll('Nizam',6503)
school.enroll('Sabbir',6507)
school.enroll('Yeamin',6576)

print(school.enroll('Irfan',6700))

# ....