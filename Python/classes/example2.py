class student:
    def __init__(self,name,roll,marks):
        self.student_name = name
        self.student_roll = roll
        self.student_marks = marks
    def average(self):
        return sum(self.student_marks)/len(self.student_marks)


s = student("bimal",1,[80,70,85])
print(s.student_name,"got", s.average())
