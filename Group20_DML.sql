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

-- browse students
SELECT Students.student_id, Students.first_name, Students.last_name, Houses.house_name AS house_name, Students.level_attending FROM Students LEFT JOIN Houses ON Students.house_id = Houses.house_id;

-- add a new student
INSERT INTO Students (first_name, last_name, house_id, level_attending) VALUES (:fnameInput, :lnameInput, :house_id_from_dropdownInput, :level_attending_from_dropdownInput);

-- get a single student's data for the update student form
SELECT * FROM Students WHERE student_id = :student_ID_selected_from_students_page;

-- update a student's data based on submission of update student form
UPDATE Students SET first_name = :fnameInput, last_name = :lnameInput, house_id = :house_id_from_dropdownInput, level_attending = :level_attending_from_dropdownInput WHERE student_id = :student_ID_from_the_update_form;

-- delete a student
DELETE FROM Students WHERE student_id = :student_ID_selected_from_students_page;

-- drop down menus
SELECT house_name FROM Houses;

--
-- for table `Professors`
--

-- browse professors
SELECT * FROM Professors;

-- add a new professor
INSERT INTO Professors (first_name, last_name) VALUES (:fnameInput, :lnameInput);

-- get a single professor's data for the update professor form
SELECT * FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page;

-- update a professor's data based on submission of update professor form
UPDATE Professors SET first_name = :fnameInput, last_name = :lnameInput WHERE professor_id = :professor_ID_from_the_update_form;

-- delete a professor
DELETE FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page;

--
-- for table `Houses`
--

-- browse houses
SELECT Houses.house_id, CONCAT(Professors.first_name, ' ', Professors.last_name) AS head_of_house, Houses.house_name, Houses.house_animal, Houses.house_colors FROM Houses LEFT JOIN Professors ON Houses.head_of_house = Professors.professor_id;

-- add a new house
INSERT INTO Houses (head_of_house, house_name, house_animal, house_colors) VALUES (:hoh_from_dropdownInput, :hnameInput, :hanimalInput, :hcolorsInput);

-- get a single house's data for the update house form
SELECT * FROM Houses WHERE house_id = :house_ID_selected_from_houses_page;

-- update a house's data based on submission of update house form
UPDATE Houses SET head_of_house = :hoh_from_dropdownInput, house_name = :hnameInput, house_animal = hanimalInput, house_colors = hcolorsInput WHERE house_id = :house_ID_from_the_update_form;

-- delete a house
DELETE FROM Houses WHERE house_id = :house_ID_selected_from_houses_page;

-- drop down menus
SELECT CONCAT(Professors.first_name, ' ', Professors.last_name) AS professor_name FROM Professors;

--
-- for table `Subjects`
--

-- browse subjects
SELECT * FROM Subjects;

-- add a new subject
INSERT INTO Subjects (subject_name, core_elective) VALUES (:snameInput, :ceInput);

-- get a single subject's data for the update subject form
SELECT * FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page;

-- update a subject's data based on submission of update subject form
UPDATE Subjects SET subject_name = :snameInput, core_elective = :ceInput WHERE subject_id = :subject_ID_from_the_update_form;

-- delete a subject
DELETE FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page;

--
-- for table `Classes`
--

-- browse classes
SELECT Classes.class_id, Subjects.subject_name AS subject_name, CONCAT(Professors.first_name, ' ', Professors.last_name) AS professor_name, Classes.class_level FROM Classes LEFT JOIN Subjects ON Classes.subject_id = Subjects.subject_id LEFT JOIN Professors ON Classes.professor_id = Professors.professor_id;

-- add a new class
INSERT INTO Classes (subject_id, professor_id, class_level) VALUES (:subid_from_dropdownInput, :profid_from_dropdownInput, :clevel_from_dropdownInput);

-- get a single class' data for the update class form
SELECT Classes.class_id, Classes.subject_id AS subject_name, Classes.professor_id AS professor_name, Classes.class_level FROM Classes WHERE class_id = :class_ID_selected_from_classes_page;

-- update a class' data based on submission of update class form
UPDATE Classes SET subject_id = :subid_from_dropdownInput, professor_id = :profid_from_dropdownInput, class_level = :clevel_from_dropdownInput WHERE class_id = :class_ID_from_the_update_form;

-- delete a class
DELETE FROM Classes WHERE class_id = :class_ID_selected_from_classes_page;

-- drop down menus
SELECT CONCAT(Professors.first_name, ' ', Professors.last_name) AS professor_name FROM Professors;
SELECT Subjects.subject_name FROM Subjects;

--
-- for table `Class_Registrations`
--

-- browse registrations
SELECT Class_Registrations.student_id, CONCAT(Students.first_name, ' ', Students.last_name) AS student_name, Class_Registrations.class_id, Subjects.subject_name, Classes.class_level, (CASE WHEN Classes.professor_id IS NULL THEN 'None' ELSE CONCAT(Professors.first_name, ' ', Professors.last_name) END) AS class_detail FROM Class_Registrations LEFT JOIN Students ON Class_Registrations.student_id = Students.student_id LEFT JOIN Classes ON Class_Registrations.class_id = Classes.class_id LEFT JOIN Subjects ON Classes.subject_id = Subjects.subject_id LEFT JOIN Professors ON Classes.professor_id = Professors.professor_id;

-- add a registration
INSERT INTO Class_Registrations (student_id, class_id) VALUES (:sid_from_dropdownInput, :cid_from_dropdownInput);

-- get a single registration's data for the update registration form
SELECT CONCAT(Students.first_name, ' ', Students.last_name) AS student_name, CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ', (CASE WHEN Classes.professor_id IS NULL THEN 'None' ELSE CONCAT(Professors.first_name, ' ', Professors.last_name) END)) AS class_detail FROM Class_Registrations LEFT JOIN Students ON Class_Registrations.student_id = Students.student_id LEFT JOIN Classes ON Class_Registrations.class_id = Classes.class_id LEFT JOIN Subjects ON Classes.subject_id = Subjects.subject_id LEFT JOIN Professors ON Classes.professor_id = Professors.professor_id WHERE Class_Registrations.student_id = :student_ID_selected_from_registrations_page and Class_Registrations.class_id = :class_ID_selected_from_registrations_page;

-- update a registration's data based on submission of update registration form
UPDATE Class_Registrations SET student_id = :sid_from_dropdownInput, class_id = :cid_from_dropdownInput WHERE student_id = :sid_from_the_update_form and class_id = :cid_from_the_update_form

-- delete a registration
DELETE FROM Class_Registrations WHERE student_id = :student_ID_selected_from_registrations_page AND class_id = :class_ID_selected_from_registrations_page;

-- drop down menus
SELECT CONCAT(Students.first_name, ' ', Students.last_name) AS student_name FROM Students;
SELECT CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ', (CASE WHEN Classes.professor_id IS NULL THEN 'None' ELSE CONCAT(Professors.first_name, ' ', Professors.last_name) END)) AS class_detail FROM Classes LEFT JOIN Subjects ON Classes.subject_id = Subjects.subject_id LEFT JOIN Professors ON Classes.professor_id = Professors.professor_id;

--
-- for helper functions
--

-- get_house_id_from_name
SELECT house_id FROM Houses WHERE house_name = %s;

-- get_house_name_from_id
SELECT house_name from Houses WHERE house_id = %s;

-- get_professor_id_from_name
SELECT professor_id FROM Professors WHERE first_name = %s AND last_name = %s;

-- get_professor_name_from_id
SELECT first_name, last_name from Professors WHERE professor_id = %s;

-- get_subject_id_from_name
SELECT subject_id FROM Subjects WHERE subject_name = %s;

-- get_subject_name_from_id
SELECT subject_name from Subjects WHERE subject_id = %s;

-- get_student_id_from_name
SELECT student_id FROM Students WHERE first_name = %s AND last_name = %s;

-- get_student_name_from_id
SELECT first_name, last_name from Students WHERE student_id = %s;

-- get_class_id_from_class_detail
SELECT class_id FROM Classes WHERE subject_id = %s AND class_level = %s AND (CASE WHEN Classes.professor_id IS NOT NULL THEN professor_id = %s ELSE ISNULL(professor_id) END);

-- get_pks_from_table
SELECT {primary_key_name} from {table_name};

-- delete_record
DELETE FROM {table_name} WHERE {primary_key_name} = '%s';