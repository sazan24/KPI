SELECT group_name, lastname, firstname, num_mark, mark
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
WHERE num_mark > (SELECT AVG(num_mark) 
			      FROM Exam_result);
			      

SELECT group_name, AVG(num_mark) AS max_group_mark
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
GROUP BY group_name	
HAVING AVG(num_mark) = (SELECT MAX(num_mark)
						FROM Exam_result)


SELECT group_name, COUNT(lastname)
FROM
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Exam_result
  ON Student.ID__student = Exam_result.ID__student
WHERE num_mark = (SELECT MAX(num_mark))
				  FROM Exam_result)
GROUP BY group_name
HAVING group_name LIKE 'та-0_';
