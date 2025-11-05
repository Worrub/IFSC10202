class Student:
    def __init__(self, firstname: str, lastname: str, tnumber: str):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Scores = [] 
    def RunningAverage(self):
        valid_scores = [s for s in self.Scores if s is not None]
        if len(valid_scores) == 0:
            return 0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        if len(self.Scores) == 0:
            return 0
        total = sum(s if s is not None else 0 for s in self.Scores)
        return total / len(self.Scores)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname: str, lastname: str, tnumber: str):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber: str):
        for i, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        print(f"{'First Name':<12} {'Last Name':<12} {'T-Number':<10} "
              f"{'Running Avg':>12} {'Semester Avg':>12} {'Grade':>8}")
        print("-" * 70)

        for s in self.Studentlist:
            print(f"{s.FirstName:<12} {s.LastName:<12} {s.TNumber:<10} "
                  f"{s.RunningAverage():>12.2f} {s.TotalAverage():>12.2f} {s.LetterGrade():>8}")

    def add_student_from_file(self, filename: str):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        firstname, lastname, tnumber = parts[0], parts[1], parts[2]
                        self.add_student(firstname, lastname, tnumber)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    def add_scores_from_file(self, filename: str):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        tnumber = parts[0]
                        scores = []
                        for s in parts[1:]:
                            if s.strip() == "":
                                scores.append(None)
                            else:
                                try:
                                    scores.append(float(s))
                                except ValueError:
                                    scores.append(None)
                        index = self.find_student(tnumber)
                        if index != -1:
                            self.Studentlist[index].Scores.extend(scores)
                        else:
                            print(f"Warning: Student with TNumber {tnumber} not found.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

#\/-------------------------- MAIN ----------------------------\/
def main():
    students = StudentList()

    students.add_student_from_file("11/11.Project Students.txt")
    students.add_scores_from_file("11/11.Project Scores.txt")

    students.print_student_list()

if __name__ == "__main__":
    main()