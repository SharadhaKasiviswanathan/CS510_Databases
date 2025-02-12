-- DDL STATEMENTS

CREATE DATABASE IF NOT EXISTS students_grades_management;
USE students_grades_management;

CREATE TABLE class (
  class_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  course_number VARCHAR(255) NOT NULL,
  term VARCHAR(255) NOT NULL,
  section_number VARCHAR(255) NOT NULL,
  class_description VARCHAR(255) NOT NULL,
  INDEX (course_number)  
);

CREATE TABLE category (
  category_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  weight DECIMAL(10,2) NOT NULL,
  class_id INTEGER NOT NULL REFERENCES class,
  FOREIGN KEY (class_id) REFERENCES class(class_id),
  INDEX (class_id) 
);

CREATE TABLE student (
  student_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email_address VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  INDEX (username) 
);

CREATE TABLE enrolled (
  class_id INTEGER NOT NULL REFERENCES class,
  student_id INTEGER NOT NULL REFERENCES student,
  FOREIGN KEY (class_id) REFERENCES class(class_id),
  FOREIGN KEY (student_id) REFERENCES student(student_id),
  PRIMARY KEY (class_id, student_id)
);

CREATE TABLE assignment (
  assignment_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  assignment_name VARCHAR(255) NOT NULL,
  point_value INTEGER NOT NULL,
  assignment_description VARCHAR(255) NOT NULL,
  category_id INTEGER NOT NULL REFERENCES category,
  class_id INTEGER NOT NULL REFERENCES class,
  FOREIGN KEY (category_id) REFERENCES category(category_id),
  FOREIGN KEY (class_id) REFERENCES class(class_id),
  INDEX (category_id), 
  INDEX (class_id) 
);

CREATE TABLE grades (
  grade DECIMAL(10,2) NOT NULL,
  student_id INTEGER NOT NULL REFERENCES student,
  assignment_id INTEGER NOT NULL REFERENCES assignment,
  FOREIGN KEY (student_id) REFERENCES student(student_id),
  FOREIGN KEY (assignment_id) REFERENCES assignment(assignment_id),
  PRIMARY KEY (student_id, assignment_id)
);

-- For checking:

select * from class;
select * from assignment;
select * from category;
select * from grades;
select * from enrolled;
select * from student;

-- Changes performed

SET SQL_SAFE_UPDATES = 0;
UPDATE category SET weight = 5 WHERE category_name = 'Quizzes';
SET SQL_SAFE_UPDATES = 1;


