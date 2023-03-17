CREATE VIEW [Відмінники] AS
SELECT group_name AS 'Назва групи', 
       lastname 'Прізвище', 
	   firstname AS 'Імена',
	   mark AS 'Результат сесії',
	   scholarship_amount AS 'Розмір стипендії'
FROM 
    Group_name JOIN Student
    ON Group_name.ID__group_name = Student.ID__group_name
    JOIN Exam_result
    ON Student.ID__student = Exam_result.ID__student
    JOIN Scholarship
    ON Exam_result.ID__student = Scholarship.ID__student
WHERE mark = 'Відмінно';


SELECT * FROM [Відмінники]

UPDATE Exam_result
SET mark = 'Добре'
WHERE ID__student = 2;

SELECT * FROM [Відмінники]


UPDATE Scholarship
SET scholarship_amount = 4200
WHERE ID__student = 8;

SELECT * FROM [Відмінники]