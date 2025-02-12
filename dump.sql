-- SAMPLE DATA INSERTION

-- Inserting sample data into the class table
INSERT INTO class (course_number, term, section_number, class_description) VALUES
('CS101', 'Spring 2023', '001', 'Introduction to Computer Science'),
('CS410', 'Fall 2023', '001', 'Databases'),
('CS510', 'Spring 2024', '002', 'Advanced Databases');

-- Inserting sample data into the category table
INSERT INTO category (category_name, weight, class_id) VALUES
('Homework', 25.0, 1),
('Quizzes', 10.0, 1),
('Midterm Exam', 15.0, 1),
('Final Exam', 20.0, 1),
('Presentation', 10.0, 2),
('Projects', 20.0, 3);

-- Inserting sample data into the student table
INSERT INTO student (username, first_name, last_name, email_address, address) VALUES
('johndoe', 'John', 'Doe', 'johndoe@example.com', '123 Main St'),
('jennydow', 'Jenny', 'Dow', 'jennydow@example.com', '456 Elm St'),
('mikesmith', 'Mike', 'Smith', 'mikesmith@example.com', '789 Oak Ave');

-- Inserting sample data into the enrolled table
INSERT INTO enrolled (class_id, student_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 1),
(3, 3);

-- Inserting sample data into the assignment table
INSERT INTO assignment (assignment_name, point_value, assignment_description, category_id, class_id) VALUES
('Homework 1', 100, 'Complete exercises 1-5', 1, 1),
('Quiz 1', 50, 'Short quiz on basic concepts', 2, 1),
('Midterm Exam', 200, 'Midterm exam covering topics 1-5', 3, 1),
('Final Exam', 250, 'Comprehensive final exam', 4, 1),
('Presentation', 100, 'Present on a literary topic', 5, 2),
('Project 1', 200, 'Create a programming project', 6, 3);



-- Inserting sample data into the grades table
INSERT INTO grades (grade, student_id, assignment_id) VALUES
(95.5, 1, 1),
(85.0, 1, 2),
(180.0, 1, 3),
(230.0, 1, 4),
(92.0, 2, 1),
(88.0, 2, 2),
(185.0, 2, 3),
(240.0, 2, 4),
(140.0, 3, 1),
(96.0, 3, 2),
(75.0, 3, 5),
(190.0, 3, 6);