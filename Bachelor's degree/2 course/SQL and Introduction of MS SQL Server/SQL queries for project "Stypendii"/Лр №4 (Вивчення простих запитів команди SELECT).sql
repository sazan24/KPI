SELECT DISTINCT mark, scholarship_amount
FROM 
  Scholarship INNER JOIN Exam_result
  ON Scholarship.ID__student = Exam_result.ID__student;


SELECT group_name, lastname, firstname, mark
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
WHERE mark = 'Відмінно';
 
 
SELECT group_name, SUM(scholarship_amount)
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Scholarship
  ON Student.ID__student = Scholarship.ID__student
GROUP BY group_name;