class marks:
    def __init__(self):
        self._roll_num = 0
        self._marks1 = 0
        self._marks2 = 0 
        self._marks3 = 0
        self._marks4 = 0
        self._totalmarks = 0
        self._percentage = 0
    def get_roll_num(self):
        return self._roll_num
    def get_marks1(self):
        return self._marks1
    def get_marks2(self):
        return self._marks2
    def get_marks3(self):
        return self._marks3
    def get_marks4(self):
        return self._marks4
    def get_totalmarks(self):
        return self._totalmarks
    def get_percentage(self):
        return self._percentage

    def set_roll_num(self, a):
        self._roll_num = a
    def set_marks1(self, b):
        self._marks1 = b
    def set_marks2(self, c):
        self._marks2 = c
    def set_marks3(self, d):
        self._marks3 = d
    def set_marks4(self, e):
        self._marks4 = e
    def set_totalmarks(self):
        
        self._totalmarks = int(self._marks1 )+int( self._marks2) + int(self._marks3 )+ int(self._marks4)
        
    def set_percentage(self):
        self._percentage = int(self.get_totalmarks())/4

    def del_roll_num(self):
        del self._roll_num
    def del_marks1(self):
        del self._marks1
    def del_marks2(self):
        del self._marks2
    def del_marks3(self):
        del self._marks3
    def del_marks4(self):
        del self._marks4
    def del_totalmarks(self):
        del self._totalmarks
    def del_percentage(self):
        del self._percentage

    roll_num = property(get_roll_num, set_roll_num, del_roll_num)
    marks1 = property(get_marks1, set_marks1, del_marks1)
    marks2 = property(get_marks2, set_marks2, del_marks2)
    marks3 = property(get_marks3, set_marks3, del_marks3)
    marks4 = property(get_marks4, set_marks4, del_marks4)
    totalmarks = property(get_totalmarks, set_totalmarks, del_totalmarks)
    percentage = property(get_percentage, set_percentage, del_percentage)

student = marks()
student.roll_num = int(input("Enter your Roll No.: "))
student.marks1 = int(input("Enter marks for subject 1: "))
student.marks2 = int(input("Enter marks for subject 2: "))
student.marks3 = int(input("Enter marks for subject 3: "))
student.marks4 = int(input("Enter marks for subject 4: "))
student.set_totalmarks()
student.set_percentage()
print("The roll no. is ", student.roll_num)
print("The marks in subject 1 is ", student.marks1)
print("The marks in subject 2 is ", student.marks2)
print("The marks in subject 3 is ", student.marks3)
print("The marks in subject 4 is", student.marks4)
print("The total marks obtained is ", student.get_totalmarks())
print("The percentage obtained is ", student.get_percentage())