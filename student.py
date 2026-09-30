class Student:
    def __init__(self,name,marks):
        self.name=name
        self.set_marks(marks)
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if new_marks>=0 and new_marks<=100:
            self.__marks=new_marks
        else:
            raise ValueError("marks should be between 0 to 100")
    def calculate_grade(self):
        if self.get_marks()>=90:
            return "A Grade"
        elif self.get_marks()>=80:
            return "B Grade"
        elif self.get_marks()>=70:
            return "C Grade"
        elif self.get_marks()>=60:
            return "D Grade"
        else:
            return "Fail"

    def display(self):
        print(f"Name:{self.name}")
        print(f"Marks:{self.get_marks()}")
        print(f"Grade:{self.calculate_grade()}")


