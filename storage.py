import json
from student import Student
class Storage:
    def __init__(self,filename):
        self.filename = filename

    def save_students(self,students):
        data=[]
        for student in students:
            student_data = {
                "name":student.name,
                "marks":student.get_marks()
            }
            data.append(student_data)

        with open(self.filename,"w") as file:
            json.dump(data,file,indent=4)

    def load_students(self):
        with open(self.filename,"r") as file:
            data=json.load(file)
        students=[]
        for student_data in data:
            student=Student(
                student_data["name"],
                student_data["marks"]
            )
            students.append(student)
        return students


