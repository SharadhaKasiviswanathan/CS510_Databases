import mysql.connector
from mysql.connector import Error
from random import choice

# Please refer README.pdf file for the comments and working of these code functionalities

class DatabaseManager:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='students_grades_management',
                user='root',
                password='skasivisw99sql!?'
            )
        except Error as e:
            print(f'Error connecting to MySQL database: {e}')

    def close_connection(self):
        if self.connection:
            self.connection.close()

class ClassManagement(DatabaseManager):
    def new_class(self, course_number, term, section_number, class_description):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            try:
                insert_query = "INSERT INTO class (course_number, term, section_number, class_description) VALUES (%s, %s, %s, %s)"
                data = (course_number, term, section_number, class_description)
                cursor.execute(insert_query, data)
                self.connection.commit()
                print("Class created in database successfully")
            except Error as e:
                print(f"Error creating class: {e}")
            finally:
                cursor.close()
    
    def random_address_generator(self):
        streets = ["EnrollmentApp St.", "Oak St.", "Park Ave.", "Broadway", "Maple St.", "Cedar St.", "Elm St.", "High St.", "1st St.", "2nd St."]
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose"]
        states = ["NY", "CA", "IL", "TX", "PA", "AZ", "TX", "CA", "TX", "CA"]
        zip_codes = ["10001", "90001", "60601", "77001", "19102", "85001", "78201", "92101", "75201", "95101"]
        street = choice(streets)
        city = choice(cities)
        state = choice(states)
        zip_code = choice(zip_codes)
        address = f"{street}, {city}, {state} {zip_code}"  # Combine address components
        return address

    def list_classes(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = """
            SELECT c.course_number, c.term, c.section_number, c.class_description, COUNT(e.student_id) AS num_students
            FROM class c
            LEFT JOIN enrolled e ON c.class_id = e.class_id
            GROUP BY c.course_number, c.term, c.section_number, c.class_description
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

    def select_class(self, course_number, term, section_number=None):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            if section_number:
                query = "SELECT class_id FROM class WHERE course_number = %s AND term = %s AND section_number = %s"
                data = (course_number, term, section_number)
            else:
                query = "SELECT class_id FROM class WHERE course_number = %s AND term = %s"
                data = (course_number, term)
            cursor.execute(query, data)
            row = cursor.fetchone()
            if row:
                class_id = row[0]
                print(f"Activated class with ID: {class_id}")
            else:
                print("Class not found")
            cursor.close()

    def show_class(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = "SELECT * FROM class WHERE class_id = %s"
            active_class_id = 1  # Assuming class ID 1 is currently active, you can modify this based on your implementation
            cursor.execute(query, (active_class_id,))
            row = cursor.fetchone()
            if row:
                print(row)
            else:
                print("No active class found")
            cursor.close()

class CategoryAssignmentManagement(DatabaseManager):
    def show_categories(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = "SELECT category_name, FORMAT(CAST(weight AS FLOAT), 2) AS weight FROM category WHERE class_id = %s"
            active_class_id = 1  # Assuming class ID 1 is currently active, you can modify this based on your implementation
            cursor.execute(query, (active_class_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

    def add_category(self, category_name, weight):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            insert_query = "INSERT INTO category (category_name, weight, class_id) VALUES (%s, %s, %s)"
            active_class_id = 1  # Assuming class ID 1 is currently active, you can modify this based on your implementation
            data = (category_name, weight, active_class_id)
            cursor.execute(insert_query, data)
            self.connection.commit()
            cursor.close()

    def show_assignments(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = """
            SELECT c.category_name, a.assignment_name, a.point_value
            FROM category c
            INNER JOIN assignment a ON c.category_id = a.category_id
            WHERE c.class_id = %s
            """
            active_class_id = 1  # Assuming class ID 1 is currently active, you can modify this based on your implementation
            cursor.execute(query, (active_class_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

    def add_assignment(self, assignment_name, category_id, description, points):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            insert_query = "INSERT INTO assignment (assignment_name, point_value, assignment_description, category_id, class_id) VALUES (%s, %s, %s, %s, %s)"
            active_class_id = 1  # Assuming class ID 1 is currently active, you can modify this based on your implementation
            data = (assignment_name, points, description, category_id, active_class_id)
            cursor.execute(insert_query, data)
            self.connection.commit()
            cursor.close()

class StudentManagement(DatabaseManager):

    def add_student(self, username, student_id=None, first_name=None, last_name=None, email_address=None, address=None, class_id=None):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            if not email_address:
                email_address = f"{username}@example.com"  # Automatically generate email address
            if not address:
                address = self.random_address_generator()  # Generate random address
            
            if class_id:
                insert_query = "INSERT INTO student (username, student_id, first_name, last_name, email_address, address, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE first_name = VALUES(first_name), last_name = VALUES(last_name), email_address = CONCAT(VALUES(username), '@example.com'), class_id = VALUES(class_id)"
                data = (username, student_id, first_name, last_name, email_address, address, class_id)
            else:
                insert_query = "INSERT INTO student (username, student_id, first_name, last_name, email_address, address) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE first_name = VALUES(first_name), last_name = VALUES(last_name), email_address = CONCAT(VALUES(username), '@example.com')"
                data = (username, student_id, first_name, last_name, email_address, address)

            cursor.execute(insert_query, data)
            self.connection.commit()
            cursor.close()


 
    def show_students(self, username=None):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            if username:
                query = """
                SELECT s.*
                FROM student s
                WHERE s.username LIKE %s
                """
                data = (f'%{username}%',)
            else:
                query = """
                SELECT s.*
                FROM student s
                INNER JOIN enrolled e ON s.student_id = e.student_id
                WHERE e.class_id = %s
                """
                active_class_id = 1  # Assuming class ID 1 is currently active, modify as needed
                data = (active_class_id,)
            cursor.execute(query, data)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                if username:
                    print(f"No student found with username '{username}' in any class.")
                else:
                    print("No students found in the active class.")
            cursor.close()



    def grade(self, assignment_name, username, grade):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = "SELECT assignment_id FROM assignment WHERE assignment_name = %s"
            cursor.execute(query, (assignment_name,))
            row = cursor.fetchone()
            if row:
                assignment_id = row[0]
                query = "SELECT student_id FROM student WHERE username = %s"
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                if row:
                    student_id = row[0]
                    insert_query = "INSERT INTO grades (student_id, assignment_id, grade) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE grade = VALUES(grade)"
                    data = (student_id, assignment_id, grade)
                    cursor.execute(insert_query, data)
                    self.connection.commit()
                    print("Grade assigned successfully")
                else:
                    print("Student not found")
            else:
                print("Assignment not found")
            cursor.close()

class GradeReporting(DatabaseManager):
  
    def student_grades(self, username):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = """
            SELECT c.category_name, SUM(a.point_value) AS total_points,
                   FORMAT(SUM(g.grade) / SUM(a.point_value) * 100, 2) AS category_grade
            FROM grades g
            INNER JOIN assignment a ON g.assignment_id = a.assignment_id
            INNER JOIN category c ON a.category_id = c.category_id
            INNER JOIN student s ON g.student_id = s.student_id
            WHERE s.username = %s
            GROUP BY c.category_name
            """
            cursor.execute(query, (username,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()


    def gradebook(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = """
            SELECT s.username, s.student_id, s.first_name, s.last_name,
                   FORMAT(SUM(g.grade) / SUM(a.point_value) * 100, 2) AS total_grade
            FROM grades g
            INNER JOIN assignment a ON g.assignment_id = a.assignment_id
            INNER JOIN student s ON g.student_id = s.student_id
            GROUP BY s.username, s.student_id, s.first_name, s.last_name
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

class GradeCalculation(DatabaseManager):
 

    def calculate_grades(self):
        self.get_connection()
        if self.connection:
            cursor = self.connection.cursor()
            query = """
            SELECT s.username, c.category_name, 
                FORMAT(SUM(g.grade) / SUM(a.point_value) * 100, 2) AS weighted_grade
            FROM grades g
            INNER JOIN assignment a ON g.assignment_id = a.assignment_id
            INNER JOIN category c ON a.category_id = c.category_id
            INNER JOIN student s ON g.student_id = s.student_id
            GROUP BY s.username, c.category_name
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                # Print formatted values directly as floats
                print(row[0], row[1], f"{float(row[2]):.2f}")
            cursor.close()

 

class FinalApp(ClassManagement, CategoryAssignmentManagement, StudentManagement, GradeReporting, GradeCalculation):
    def __init__(self):
        super().__init__()

    def execute_command(self, command):
        print("-----------------------------------------------------------")

        command_parts = command.split()
        if len(command_parts) == 0:
            print("Invalid command")
            return

        command_type = command_parts[0].lower()

        if command_type == 'new-class': 
            if len(command_parts) == 5:
                _, course_number, term, section_number, class_description = command_parts
                self.new_class(course_number, term, section_number, class_description)
                print("Check the created class in database")
            else:
                print("Invalid number of arguments for create-class command")
        elif command_type == 'list-classes' and len(command_parts) == 1:
            self.list_classes()

        elif command_type == 'select-class' and len(command_parts) in (2, 3):
            if len(command_parts) == 2:
                _, course_number = command_parts
                self.select_class(course_number, None)  # Passing None for term
            elif len(command_parts) == 3:
                _, course_number, term = command_parts
                if term.isdigit():  # Specific section case
                    _, course_number, term, section_number = command_parts
                    self.select_class(course_number, term, section_number)
                else:  # Fall 2018 case
                    self.select_class(course_number, term)
        elif command_type == 'show-class' and len(command_parts) == 1:
            self.show_class()
        elif command_type == 'show-categories' and len(command_parts) == 1:
            self.show_categories()
        elif command_type == 'add-category' and len(command_parts) == 3:
            _, category_name, weight = command_parts
            self.add_category(category_name, float(weight))
            print("Category added successfully")
        elif command_type == 'show-assignment' and len(command_parts) == 1:
            self.show_assignments()
        elif command_type == 'add-assignment' and len(command_parts) == 5:
            _, assignment_name, category, description, points = command_parts
            self.add_assignment(assignment_name, int(category), description, int(points))
            print("Assignment added successfully")
        elif command_type == 'add-student' and len(command_parts) in (4, 5):
            _, username, studentid, last_name, first_name = command_parts
            if len(command_parts) == 4:
                self.add_student(username)
            else:
                self.add_student(username, int(studentid), last_name, first_name)
            print("Student added/enrolled successfully")


        elif command_type == 'show-students' and len(command_parts) in (1, 2):
            if len(command_parts) == 1:
                self.show_students()
            else:
                _, filter_string = command_parts
                self.show_students(filter_string)


        elif command_type == 'grade' and len(command_parts) == 4:
            _, assignment_name, username, grade = command_parts
            self.grade(assignment_name, username, float(grade))
            print("Verify grade in database")
        elif command_type == 'student-grades' and len(command_parts) == 2:
            _, username = command_parts
            self.student_grades(username)
        elif command_type == 'gradebook' and len(command_parts) == 1:
            self.gradebook()
        elif command_type == 'calculate-grades' and len(command_parts) == 1:
            self.calculate_grades()
            print("Grades calculated successfully")
        else:
            print("Invalid command. Please enter a valid command.")

# Example usage
app = FinalApp()

while True:
    command = input("Enter command: ")
    if command.lower() == 'exit':
        break
    app.execute_command(command)
