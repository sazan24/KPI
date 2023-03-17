CREATE VIEW [Розмір стипендії відповідно до результату здачі сесії] AS
SELECT DISTINCT mark AS 'Результат сесії', 
				scholarship_amount AS 'Розмір стипендії'
FROM 
  Scholarship INNER JOIN Exam_result
  ON Scholarship.ID__student = Exam_result.ID__student;

SELECT * FROM [Розмір стипендії відповідно до результату здачі сесії]


CREATE VIEW [ПІБ та назва групи відмінників] AS
SELECT group_name AS 'Назва групи', 
       lastname 'Прізвище', 
	   firstname AS 'Імена',
	   mark AS 'Результат сесії'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
WHERE mark = 'Відмінно';
 
SELECT * FROM [ПІБ та назва групи відмінників]


CREATE VIEW [Сума стипендії по групах] AS
SELECT group_name AS 'Назва групи', 
       SUM(scholarship_amount) AS 'Сума стипендій'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Scholarship
  ON Student.ID__student = Scholarship.ID__student
GROUP BY group_name;

SELECT * FROM [Сума стипендії по групах]
