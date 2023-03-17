ALTER TABLE Exam_result
	ADD CONSTRAINT Check_result CHECK(mark IN ('Не здав', 'Задовільно', 'Добре', 'Відмінно'));


ALTER TABLE Student
	ADD CONSTRAINT StudentForeign FOREIGN KEY (ID__group_name) REFERENCES Group_name(ID__group_name); 


ALTER TABLE Student
	NOCHECK CONSTRAINT StudentForeign;

INSERT INTO Student VALUES (10, 'Петренко', 'Роман', 'Олександрович');

ALTER TABLE Student
	CHECK CONSTRAINT StudentForeign;



DELETE FROM Student 

ALTER TABLE Student 
	CHECK CONSTRAINT StudentForeign;


ALTER TABLE Exam_result
	NOCHECK CONSTRAINT Exam_markCheck;

DELETE FROM Exam_result WHERE mark NOT IN ('Не здав', 'Задовільно', 'Добре', 'Відмінно');

ALTER TABLE Exam_result
	WITH CHECK
		CHECK CONSTRAINT  Exam_markCheck;


ALTER TABLE Student
	ADD Single VARCHAR(3) DEFAULT 'Так';

ALTER TABLE Student
	DROP CONSTRAINT DF__Student__Single__5DCAEF64;

ALTER TABLE Student
	DROP COLUMN Single


EXEC SP_RENAME 'Group_name', 'Name_of_group';


EXEC SP_RENAME 'Name_of_group', 'Group_name';
