CREATE VIEW [³�������] AS
SELECT group_name AS '����� �����', 
       lastname '�������', 
	   firstname AS '�����',
	   mark AS '��������� ���',
	   scholarship_amount AS '����� ������䳿'
FROM 
    Group_name JOIN Student
    ON Group_name.ID__group_name = Student.ID__group_name
    JOIN Exam_result
    ON Student.ID__student = Exam_result.ID__student
    JOIN Scholarship
    ON Exam_result.ID__student = Scholarship.ID__student
WHERE mark = '³�����';


SELECT * FROM [³�������]

UPDATE Exam_result
SET mark = '�����'
WHERE ID__student = 2;

SELECT * FROM [³�������]


UPDATE Scholarship
SET scholarship_amount = 4200
WHERE ID__student = 8;

SELECT * FROM [³�������]