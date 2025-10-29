class Student:
    def __init__(self, firstname: str, lastname: str, tnumber: str):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  

    def RunningAverage(self) -> float:
        valid_scores = [float(g) for g in self.Grades if g.strip() != ""]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self) -> float:
        total_scores = [float(g) if g.strip() != "" else 0.0 for g in self.Grades]
        if not total_scores:
            return 0.0
        return sum(total_scores) / len(total_scores)

    def LetterGrade(self) -> str:
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


def main():
    filename = "10/10.Project Student Scores.txt"

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 4:
                    continue  

                firstname, lastname, tnumber = parts[0], parts[1], parts[2]
                grades = parts[3:]

                student = Student(firstname, lastname, tnumber)
                student.Grades = grades

                run_avg = student.RunningAverage()
                total_avg = student.TotalAverage()
                letter = student.LetterGrade()

                print(f"Student: {student.FirstName} {student.LastName} ({student.TNumber})")
                print(f"  Running Average: {run_avg:.2f}")
                print(f"  Total Average:   {total_avg:.2f}")
                print(f"  Letter Grade:    {letter}")
                print("-" * 40)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == "__main__":
    main()
