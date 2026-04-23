Project Description
This is a Python-based Employee Management System designed to demonstrate the core pillars of Object-Oriented Programming (OOP). The application provides a command-line interface to manage different types of organizational roles, ensuring data security through encapsulation and code reusability through inheritance.

Key Features & OOP Implementation
Encapsulation: Sensitive data like Employee ID and Salary are stored as private members (using the __ prefix) and are accessed or modified only through secure getter and setter methods.

Inheritance: A hierarchical structure where the Manager and Developer classes inherit common attributes (Name, Age) from the base Employee class.

Method Overriding: The display() method is customized in each subclass to show role-specific information, such as "Department" for Managers or "Programming Language" for Developers.

Method Overloading (Logic): The constructor in the base class is designed to handle different initialization scenarios, such as creating a basic person without an ID or salary.

Resource Management: Includes a destructor (__del__) to signify the cleanup of objects when they are removed from memory.

System Requirements
Language: Python 3.x (The system was successfully verified on Python 3.14).

Environment: Any standard IDE or terminal (e.g., VS Code, PyCharm).

Usage Instructions
Run the script: Execute project5.py in your terminal.

Navigate the Menu:

Option 1: Create a basic record with only Name and Age.

Option 2: Create a full Employee record including ID and Salary.

Option 3: Create a Manager record with specific Department details.

Option 4: Display the details of any created entity.

Option 5: Securely exit the system.


https://drive.google.com/file/d/1nur96g6rt7N139udCG6qGQgBFUNfrzIf/view?usp=drive_link
