ALTER TABLE Exam_result
  ADD num_mark INT;


UPDATE Exam_result
SET num_mark = 2
WHERE mark='Не здав';

UPDATE Exam_result
SET num_mark = 3
WHERE mark='Задовільно';

UPDATE Exam_result
SET num_mark = 4
WHERE mark='Добре';

UPDATE Exam_result
SET num_mark = 5
WHERE mark='Відмінно';


SELECT * FROM Exam_result