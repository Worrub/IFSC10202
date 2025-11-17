class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):
        if not str(emp_num).isdigit():
            raise ValueError("Employee number must be an integer.")
        if not first or not last or not address or not city:
            raise ValueError("First, Last, Address, and City are required.")
        if not (state.isupper() and len(state) == 2):
            raise ValueError("State must be 2 uppercase letters.")
        if not (zip_code.isdigit() and len(zip_code) == 5):
            raise ValueError("Zip must be 5 digits.")

        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code

class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []

    def ReadEmployeeFile(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = [p.strip() for p in line.split(",")]
                    emp = Employee(*parts)
                    self.employees.append(emp)
        except FileNotFoundError:
            print("Employee file not found. Starting with an empty list.")

    def WriteEmployeeFile(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp.emp_num}, {emp.first}, {emp.last}, "
                           f"{emp.address}, {emp.city}, {emp.state}, {emp.zip}\n")
        print("Changes Saved.")

    def DisplayEmployeeList(self):
        print()
        print("Employee        First           Last            Address         City            State           Zip")
        print("Number          Name            Name")
        print("--------------- --------------- --------------- --------------- --------------- --------------- ---------------")

        for emp in self.employees:
            print(f"{emp.emp_num:<15} {emp.first:<15} {emp.last:<15} "
                  f"{emp.address:<15} {emp.city:<15} {emp.state:<15} {emp.zip:<15}")
        print()

    def FindEmployee(self, emp_num):
        for i, emp in enumerate(self.employees):
            if emp.emp_num == emp_num:
                return i
        return -1

    def ReadEmployee(self, emp_num):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            return None
        emp = self.employees[idx]
        return emp.emp_num, emp.first, emp.last, emp.address, emp.city, emp.state, emp.zip

    def NextEmployeeNumber(self):
        if not self.employees:
            return 1
        return self.employees[-1].emp_num + 1

    def AddEmployee(self, first, last, address, city, state, zip_code):
        new_num = self.NextEmployeeNumber()
        emp = Employee(new_num, first, last, address, city, state, zip_code)
        self.employees.append(emp)
        print("Employee Added")

    def UpdateEmployee(self, emp_num, first, last, address, city, state, zip_code):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            print("Employee not found.")
            return

        emp = self.employees[idx]
        emp.first = first
        emp.last = last
        emp.address = address
        emp.city = city
        emp.state = state
        emp.zip = zip_code

    def DeleteEmployee(self, emp_num):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            print("Employee not found.")
            return
        del self.employees[idx]
        print("Employee Deleted")

def main():
    emp_list = EmployeeList("Final Project Employees.txt")
    emp_list.ReadEmployeeFile()

    while True:
        print("(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit\n")

        choice = input("Enter Selection: ").upper()

        if choice == "A":
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ").upper()
            zip_code = input("Enter Zip: ")

            try:
                emp_list.AddEmployee(first, last, address, city, state, zip_code)
            except ValueError as e:
                print("Error:", e)

        elif choice == "D":
            try:
                num = int(input("Enter Employee Number: "))
                emp_list.DeleteEmployee(num)
            except ValueError:
                print("Invalid number.")

        elif choice == "C":
            try:
                num = int(input("Enter Employee Number: "))
            except ValueError:
                print("Invalid number.")
                continue

            idx = emp_list.FindEmployee(num)
            if idx == -1:
                print("Employee not found.")
                continue

            while True:
                print("\n(F)irst Name")
                print("(L)Last Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack to Main Menu\n")

                ch = input("Enter Selection: ").upper()

                emp = emp_list.employees[idx]

                if ch == "F":
                    emp.first = input("Enter First Name: ")
                elif ch == "L":
                    emp.last = input("Enter Last Name: ")
                elif ch == "A":
                    emp.address = input("Enter Address: ")
                elif ch == "C":
                    emp.city = input("Enter City: ")
                elif ch == "S":
                    emp.state = input("Enter State: ").upper()
                elif ch == "Z":
                    emp.zip = input("Enter Zip: ")
                elif ch == "B":
                    break
                else:
                    print("Invalid selection.")

        elif choice == "P":
            emp_list.DisplayEmployeeList()

        elif choice == "S":
            emp_list.WriteEmployeeFile()

        elif choice == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid selection.\n")

main()
