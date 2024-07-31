
-- add a new student
INSERT INTO Students (first_name, last_name, house_id, level_attending) VALUES (:fnameInput, :lnameInput, :house_id_from_dropdownInput, :level_attendingInput)

-- find a student id by first and last name
SELECT student_id FROM Students WHERE first_name = :fnameInput AND last_name = :lnameInput

-- get a single student's data for the update student form
SELECT student_id, first_name, last_name, house_id, level_attending FROM Students WHERE student_id = :student_ID_selected_from_students_page

-- delete a student
DELETE FROM Students WHERE student_id = :student_ID_selected_from_students_page

-- add a new professor
INSERT INTO Professors (first_name, last_name) VALUES (:fnameInput, :lnameInput)

-- get a single professor's data for the update professor form
SELECT professor_id, first_name, last_name FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page

-- delete a professor
DELETE FROM Professors WHERE professor_id = :professor_ID_selected_from_professors_page

-- add a new house
INSERT INTO Houses (head_of_house, house_name, house_animal, house_colors) VALUES (:hohInput, :hnameInput, :hanimalInput, :hcolorsInput)

-- get a single house's data for the update house form
SELECT house_id, head_of_house, house_name, house_animal, house_colors FROM Houses WHERE house_id = :house_ID_selected_from_houses_page

-- delete a house
DELETE FROM Houses WHERE house_id = :house_ID_selected_from_houses_page

-- add a new subject
INSERT INTO Subjects (subject_name, core_elective) VALUES (:snameInput, :ceInput)

-- get a single subject's data for the update subject form
SELECT subject_id, subject_name, core_elective FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page

-- delete a subject
DELETE FROM Subjects WHERE subject_id = :subject_ID_selected_from_subjects_page

-- add a new class
INSERT INTO Classes (subject_id, professor_id, class_level) VALUES (:subidInput, :profidInput, :clevelInput)

-- get a single class' data for the update class form
SELECT class_id, subject_id, class_level FROM Classes WHERE class_id = :class_ID_selected_from_classes_page

-- delete a class
DELETE FROM Classes WHERE class_id = :class_ID_selected_from_classes_page

-- add a registration
INSERT INTO Class_Registrations (student_id, class_id) VALUES (:sidInput, :cidInput)

-- delete a registration
DELETE FROM Class_Registrations WHERE student_id = :student_ID_selected_from_registrations_page AND class_id = :class_ID_selected_from_registrations_page

-- find all students in a class  
SELECT student_id FROM Class_Registrations WHERE class_id = :class_ID_selected_from_registrations_page

-- find all registrations by a student
SELECT class_id FROM Class_Registrations WHERE student_id = :student_ID_selected_from_registrations_page
