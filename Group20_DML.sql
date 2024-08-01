--
-- Group: 20
-- Team members: 
-- Austin Cooper, Team Leader, Researcher, and Deadline Enforcer
-- Wei-Yin Chen, Creativity Officer, Ed Discussion liaison and Submission Proofreader
--

--
-- Database: `Hogwarts_Course_Registration_System`
--

-- --------------------------------------------------------

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

--
-- for table `Students`
--

-- add a new student, and enroll that student in required History of Magic for First Years
INSERT INTO Students (first_name, last_name, house_id, level_attending) VALUES (:fnameInput, :lnameInput, :house_id_from_dropdownInput, :level_attendingInput);
INSERT INTO Class_Registrations(student_id, class_id)
    SELECT LAST_INSERT_ID(), class_id
    FROM Classes
        WHERE subject_id = (SELECT subject_id FROM Subjects WHERE subject_name='History of Magic') AND class_level = 1;

-- find a student id by first and last name
SELECT student_id FROM Students WHERE first_name = :fnameInput AND last_name = :lnameInput;

-- get a single student's data for the update student form
SELECT student_id, first_name, last_name, house_id, level_attending FROM Students WHERE student_id = :student_ID_selected_from_students_page;

-- Update a student's data based on submission of update student form
UPDATE Students SET first_name = :fnameInput, last_name = :lnameInput, house_id = :house_id_from_dropdownInput, level_attending = :level_attendingInput WHERE student_id = :student_ID_from_the_update_form;

-- delete a student
DELETE FROM Students WHERE student_id = :student_ID_selected_from_students_page;

--
-- for table `Professors`
--

-- add a new professor
INSERT INTO Professors (first_name, last_name) VALUES (:fnameInput, :lnameInput);

-- get a single professor's data for the update professor form
SELECT professor_id, first_name, last_name FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page;

-- Update a professor's data based on submission of update professor form
UPDATE Professors SET first_name = :fnameInput, last_name = :lnameInput WHERE professor_id = :professor_ID_from_the_update_form;

-- delete a professor
DELETE FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page;

--
-- for table `Houses`
--

-- add a new house
INSERT INTO Houses (head_of_house, house_name, house_animal, house_colors) VALUES (:hohInput, :hnameInput, :hanimalInput, :hcolorsInput);

-- get a single house's data for the update house form
SELECT house_id, head_of_house, house_name, house_animal, house_colors FROM Houses WHERE house_id = :house_ID_selected_from_houses_page;

-- Update a house's data based on submission of update house form
UPDATE Houses SET head_of_house = :hohInput, house_name = :hnameInput, house_animal = hanimalInput, house_colors = hcolorsInput WHERE house_id = :house_ID_from_the_update_form;

-- delete a house
DELETE FROM Houses WHERE house_id = :house_ID_selected_from_houses_page;

--
-- for table `Subjects`
--

-- add a new subject
INSERT INTO Subjects (subject_name, core_elective) VALUES (:snameInput, :ceInput);

-- get a single subject's data for the update subject form
SELECT subject_id, subject_name, core_elective FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page;

-- Update a subject's data based on submission of update subject form
UPDATE Subjects SET subject_name = :snameInput, core_elective = :ceInput WHERE subject_id = :subject_ID_from_the_update_form;

-- delete a subject
DELETE FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page;

--
-- for table `Classes`
--

-- add a new class
INSERT INTO Classes (subject_id, professor_id, class_level) VALUES (:subidInput, :profidInput, :clevelInput);

-- get a single class' data for the update class form
SELECT class_id, subject_id, class_level FROM Classes WHERE class_id = :class_ID_selected_from_classes_page;

-- Update a class' data based on submission of update class form
UPDATE Classes SET subject_id = :subidInput, professor_id = :profidInput, class_level = :clevelInput WHERE class_id = :class_ID_from_the_update_form;

-- delete a class
DELETE FROM Classes WHERE class_id = :class_ID_selected_from_classes_page;

--
-- for table `Class_Registrations`
--

-- add a registration
INSERT INTO Class_Registrations (student_id, class_id) VALUES (:sidInput, :cidInput);

-- delete a registration
DELETE FROM Class_Registrations WHERE student_id = :student_ID_selected_from_registrations_page AND class_id = :class_ID_selected_from_registrations_page;

-- find all students in a class  
SELECT student_id FROM Class_Registrations WHERE class_id = :class_ID_selected_from_registrations_page;

-- find all registrations by a student
SELECT class_id FROM Class_Registrations WHERE student_id = :student_ID_selected_from_registrations_page;
