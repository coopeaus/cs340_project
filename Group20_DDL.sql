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
-- Table structure for table `Students`
--

CREATE OR REPLACE TABLE Students (
    student_id int(11) NOT NULL UNIQUE AUTO_INCREMENT,
    house_id int(11) NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    level_attending int(11) NOT NULL,
    PRIMARY KEY (student_id),
    FOREIGN KEY (house_id) REFERENCES Houses(house_id) ON DELETE CASCADE
);

--
-- Table structure for table `Professors`
--

CREATE OR REPLACE TABLE Professors (
    professor_id int(11) NOT NULL UNIQUE AUTO_INCREMENT,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    PRIMARY KEY (professor_id)
);

--
-- Table structure for table `Houses`
--

CREATE OR REPLACE TABLE Houses (
    house_id int(11) NOT NULL UNIQUE AUTO_INCREMENT,
    head_of_house int(11) NOT NULL,
    house_name varchar(255) NOT NULL,
    house_animal varchar(255) NOT NULL,
    house_colors varchar(255) NOT NULL,
    PRIMARY KEY (house_id),
    FOREIGN KEY (head_of_house) REFERENCES Professors(professor_id) ON DELETE CASCADE
);

--
-- Table structure for table `Subjects`
--

CREATE OR REPLACE TABLE Subjects (
    subject_id int(11) NOT NULL UNIQUE AUTO_INCREMENT,
    subject_name varchar(255) NOT NULL,
    core_elective int(11) NOT NULL,
    PRIMARY KEY (subject_id)
);

--
-- Table structure for table `Classes`
--

CREATE OR REPLACE TABLE Classes (
    class_id int(11) NOT NULL UNIQUE AUTO_INCREMENT,
    subject_id int(11) NOT NULL,
    professor_id int(11),
    class_level int(11) NOT NULL,
    PRIMARY KEY (class_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id) ON DELETE CASCADE
);

--
-- Table structure for table `Class_Registrations`
--

CREATE OR REPLACE TABLE Class_Registrations (
    student_id int(11) NOT NULL,
    class_id int(11) NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id) ON DELETE CASCADE
);

--
-- Dumping data for table `Professors`
--

INSERT INTO Professors (first_name, last_name)
VALUES
('Minerva', 'McGonagall'),
('Pomona', 'Sprout'),
('Filius', 'Flitwick'),
('Severus', 'Snape');

--
-- Dumping data for table `Houses`
--

INSERT INTO Houses (head_of_house, house_name, house_animal, house_colors)
VALUES
((SELECT professor_id FROM Professors WHERE first_name = 'Minerva' AND last_name = 'McGonagall'), 'Gryffindor', 'Lion', 'Scarlet and gold'),
((SELECT professor_id FROM Professors WHERE first_name = 'Pomona' AND last_name = 'Sprout'), 'Hufflepuff', 'Badger', 'Yellow and black'),
((SELECT professor_id FROM Professors WHERE first_name = 'Filius' AND last_name = 'Flitwick'), 'Ravenclaw', 'Eagle', 'Blue and bronze'),
((SELECT professor_id FROM Professors WHERE first_name = 'Severus' AND last_name = 'Snape'), 'Slytherin', 'Snake', 'Green and silver');

--
-- Dumping data for table `Subjects`
--

INSERT INTO Subjects (subject_name, core_elective)
VALUES
('Transfiguration', 1),
('Defense Against the Dark Arts', 1),
('Charms', 1), 
('Potions', 1),
('Astronomy', 1),
('History of Magic', 1),
('Herbology', 1),
('Arithmancy', 0),
('Muggle Studies', 0),
('Divination', 0),
('Study of Ancient Runes', 0),
('Care of Magical Creatures', 0);

--
-- Dumping data for table `Students`
--

INSERT INTO Students (house_id, first_name, last_name, level_attending)
VALUES
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Hermione', 'Granger', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Neville', 'Longbottom', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Harry', 'Potter', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Fred', 'Weasley', 7),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'George', 'Weasley', 7),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Ginny', 'Weasley', 4),
((SELECT house_id FROM Houses WHERE house_name = 'Gryffindor'), 'Ron', 'Weasley', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Hufflepuff'), 'Cedric', 'Diggory', 7),
((SELECT house_id FROM Houses WHERE house_name = 'Hufflepuff'), 'Hannah', 'Abbott', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Ravenclaw'), 'Cho', 'Chang', 6),
((SELECT house_id FROM Houses WHERE house_name = 'Ravenclaw'), 'Luna', 'Lovegood', 4),
((SELECT house_id FROM Houses WHERE house_name = 'Slytherin'), 'Draco', 'Malfoy', 5),
((SELECT house_id FROM Houses WHERE house_name = 'Slytherin'), 'Vincent', 'Crabbe', 5);

--
-- Dumping data for table `Classes`
--

INSERT INTO Classes (subject_id, professor_id, class_level)
VALUES
(1, 1, 1),
(1, 1, 2),
(1, 1, 3),
(1, 1, 4),
(1, 1, 5),
(7, 2, 1),
(7, 2, 2),
(7, 2, 3),
(7, 2, 4),
(7, 2, 5),
(3, 3, 1),
(3, 3, 2),
(3, 3, 3),
(3, 3, 4),
(3, 3, 5),
(4, 4, 1),
(4, 4, 2),
(4, 4, 3),
(4, 4, 4),
(4, 4, 5);

--
-- Dumping data for table `Class_Registration`
--

INSERT INTO Class_Registrations (student_id, class_id)
VALUES
(1, 5),
(1, 10),
(1, 15),
(1, 20),
(2, 5),
(2, 10),
(2, 15),
(2, 20),
(3, 5),
(3, 10),
(3, 15),
(3, 20),
(7, 5),
(7, 10),
(7, 15),
(7, 20),
(9, 5),
(9, 10),
(9, 15),
(9, 20),
(12, 5),
(12, 10),
(12, 15),
(12, 20),
(13, 5),
(13, 10),
(13, 15),
(13, 20),
(6, 4),
(6, 9),
(6, 14),
(6, 19),
(11, 4),
(11, 9),
(11, 14),
(11, 19);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;