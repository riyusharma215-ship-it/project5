class Employee:
    """Base class for all employees."""
    def __init__(self, name, age, employee_id=None, salary=None):
        # Method Overloading: Handles creation with or without ID/Salary
        self.name = name
        self.age = age
        # Encapsulation: Making sensitive data private with __
        self.__employee_id = employee_id
        self.__salary = salary

    # Getters and Setters for encapsulated data
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary = amount

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.__employee_id:
            print(f"Employee ID: {self.__employee_id}")
        if self.__salary:
            print(f"Salary: ${float(self.__salary)}")

    def __del__(self):
        """Destructor to clean up resources."""
        # In a simple script, this just prints a message when the object is deleted
        pass


class Manager(Employee):
    """Derived class for Managers."""
    def __init__(self, name, age, employee_id, salary, department):
        # Use super() to call the parent constructor
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        # Override display to include department information
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    """Derived class for Developers."""
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        # Override display to include programming language
        super().display()
        print(f"Programming Language: {self.programming_language}")


def main():
    """Main menu-driven interface."""
    storage = {
        "person": None,
        "employee": None,
        "manager": None
    }

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person (Basic Employee)")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            storage["person"] = Employee(name, age)
            print(f"\nPerson created with name: {name} and age: {age}.")

        elif choice == '2':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input("Enter Salary: ")
            storage["employee"] = Employee(name, age, emp_id, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}")

        elif choice == '3':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            emp_id = input("Enter Employee ID: ")
            salary = input("Enter Salary: ")
            dept = input("Enter Department: ")
            storage["manager"] = Manager(name, age, emp_id, salary, dept)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}")

        elif choice == '4':
            print("\nChoose details to show:")
            print("1. Person\n2. Employee\n3. Manager")
            sub_choice = input("Enter your choice: ")
            
            target = None
            if sub_choice == '1': target = storage["person"]
            elif sub_choice == '2': target = storage["employee"]
            elif sub_choice == '3': target = storage["manager"]

            if target:
                print(f"\n--- Details ---")
                target.display()
                # Use isinstance() or issubclass() to verify types as per instructions
                if isinstance(target, Manager):
                    print("(Verified: This object is a subclass of Employee)")
            else:
                print("\nNo data found for that selection.")

        elif choice == '5':
            print("\nExiting the system. All resources have been freed.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()