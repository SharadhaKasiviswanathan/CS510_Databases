# Student Grade Management System

## Overview
The **Student Grade Management System** is a Python application that allows users to manage classes, categories, assignments, students, grades, and grade calculations within a database. It provides a command-line interface for executing various functionalities ranging from student enrollment to grading.

## Requirements
- Python 3.x
- MySQL Workbench (Database)
- MySQL Connector
- Python Libraries

## Database Schema
The `students_grades_management` database consists of the following tables:

### **1. Class Table**
Represents a class and includes related information with the following columns:
- `class_id`
- `term`
- `course_number`
- `section_number`
- `class_description`

**Important:** The `term` must be entered in the specific format below to ensure proper functionality:
- `Fall2023` for Fall 2023
- `Spring2023` for Spring 2023
- `Summer2023` for Summer 2023

### **2. Category Table**
Defines different grading categories within a class with the following columns:
- `category_id`
- `weight`
- `category_name`
- `class_id`

**Important:** Weight must be entered as a decimal value (e.g., `25.00` for 25%). Ignore any Python representation such as `Decimal('100')`.

### **3. Student Table**
Stores student information with these columns:
- `student_id`
- `username`
- `first_name`
- `last_name`
- `email_address`
- `address`

### **4. Assignment Table**
Represents assignments given in a class with the following columns:
- `assignment_id`
- `assignment_name`
- `assignment_description`
- `point_value`
- `class_id`
- `category_id`

### **5. Grades Table**
Stores student grades for assignments with these columns:
- `student_id`
- `assignment_id`
- `grade`

### **6. Enrolled Table**
Tracks enrollment of students in classes with the following columns:
- `student_id`
- `class_id`

## Implementation and Execution
### **Possible Limitations**
1. **Incorrect Term Format**: The system will not function properly if the term is not entered as specified.
2. **Command Line Input Restrictions**:
   - Spaces are not accepted between inputs.
   - Use `_` (underscore) instead of spaces when naming assignments (e.g., `Homework_1`).

## Installation & Setup
### **1. Install MySQL Connector for Python**
Run the following command:
```bash
pip install mysql-connector-python
```
This package enables communication between Python and MySQL databases.

### **2. Connect Python Code with MySQL Database**
Ensure the MySQL Connector is installed and update the `DatabaseManager` class with the correct database credentials.

### **3. Development Environment**
- **Editor**: Visual Studio Code (VS Code)
- **Database**: MySQL Workbench
- **Python Version**: 3.9

### **4. Database Design**
- MySQL Workbench was used to define the database schema, tables, and relationships.

### **5. Workflow**
- Python code handles database operations, class enrollment, grading, and grade calculations.
- Integration of MySQL Workbench, Python 3.9, and VS Code for development.

## Python Class Structure
### **1. DatabaseManager Class**
Handles database connections.
- `get_connection()`: Establishes a connection to the MySQL database.
- `close_connection()`: Closes the database connection.

### **2. ClassManagement Class**
Manages class-related functionalities.
- `create_class(course_number, term, section_number, class_description)`: Creates a new class.
- `random_address_generator()`: Generates a random address.
- `list_classes()`: Lists available classes.
- `select_class(course_number, term, section_number)`: Activates a specific class.
- `show_class()`: Displays active class details.

### **3. CategoryAssignmentManagement Class**
Handles category and assignment operations.
- `show_categories()`: Displays categories in a class.
- `add_category(category_name, weight)`: Adds a category to a class.
- `show_assignments()`: Lists assignments in a class.
- `add_assignment(assignment_name, category_id, description, points)`: Adds an assignment.

### **4. StudentManagement Class**
Manages student-related operations.
- `add_student(username, student_id, first_name, last_name, email_address, address, class_id)`: Adds or updates student information.
- `show_students(username)`: Displays student details.
- `grade(assignment_name, username, grade)`: Assigns a grade to a student.

### **5. GradeReporting Class**
Provides grade reporting functionalities.
- `student_grades(username)`: Displays a specific student’s grades.
- `gradebook()`: Displays the full class gradebook.

### **6. GradeCalculation Class**
Calculates student grades.
- `calculate_grades()`: Computes final grades based on assignments and categories.

### **7. FinalApp Class**
Integrates all functionalities.
- `execute_command(command)`: Executes various commands to manage classes, students, and grades.

**Note:** Classes `2` to `6` inherit from `DatabaseManager`, and `FinalApp` inherits from all the other classes.

## Instructions to Run the Code
1. Ensure Python is installed.
2. Save the provided Python code in a file, e.g., `grades_management_app.py`.
3. Install MySQL Connector if not installed:
   ```bash
   pip install mysql-connector-python
   ```
4. Modify the database connection details in `DatabaseManager` according to your MySQL setup:
   ```python
   host='localhost'
   database='students_grades_management'
   user='root'
   password='REPLACEME'
   ```
5. Run the application from any Python-supported editor (e.g., VS Code).
