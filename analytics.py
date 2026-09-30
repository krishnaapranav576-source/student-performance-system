class Analytics:
    def __init__(self,students):
        self.students=students

    def calculate_average(self):
        if not self.students:
            raise ValueError("No students available")
        total=0
        for student in self.students:
            total+=student.get_marks()
        average=total/len(self.students)
        return average
    def highest_marks(self):
        if not self.students:
            raise ValueError("No students available")
        highest=self.students[0]
        for student in self.students:
            if student.get_marks()>highest.get_marks():
                highest=student
        return highest
    def lowest_marks(self):
        if not self.students:
            raise ValueError("No students available")
        lowest=self.students[0]
        for student in self.students:
            if student.get_marks()<lowest.get_marks():
                lowest=student
        return lowest

    def pass_fail_count(self):
        passed=0
        failed=0
        for student in self.students:
            if student.get_marks()>=60:
                passed+=1
            else:
                failed+=1
        return passed,failed
    def grade_statistics(self):
        grade_counts = {
        "A Grade": 0,
        "B Grade": 0,
        "C Grade": 0,
        "D Grade": 0,
        "Fail": 0
        }
        for student in self.students:
            grade=student.calculate_grade()
            grade_counts[grade]+=1

        return grade_counts

