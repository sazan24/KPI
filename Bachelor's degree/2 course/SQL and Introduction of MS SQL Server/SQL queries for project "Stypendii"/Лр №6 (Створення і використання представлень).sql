CREATE VIEW [����� ������䳿 �������� �� ���������� ����� ���] AS
SELECT DISTINCT mark AS '��������� ���', 
				scholarship_amount AS '����� ������䳿'
FROM 
  Scholarship INNER JOIN Exam_result
  ON Scholarship.ID__student = Exam_result.ID__student;

SELECT * FROM [����� ������䳿 �������� �� ���������� ����� ���]


CREATE VIEW [ϲ� �� ����� ����� ��������] AS
SELECT group_name AS '����� �����', 
       lastname '�������', 
	   firstname AS '�����',
	   mark AS '��������� ���'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
WHERE mark = '³�����';
 
SELECT * FROM [ϲ� �� ����� ����� ��������]


CREATE VIEW [���� ������䳿 �� ������] AS
SELECT group_name AS '����� �����', 
       SUM(scholarship_amount) AS '���� ��������'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Scholarship
  ON Student.ID__student = Scholarship.ID__student
GROUP BY group_name;

SELECT * FROM [���� ������䳿 �� ������]
