ALTER TABLE Exam_result
  ADD num_mark INT;


UPDATE Exam_result
SET num_mark = 2
WHERE mark='�� ����';

UPDATE Exam_result
SET num_mark = 3
WHERE mark='���������';

UPDATE Exam_result
SET num_mark = 4
WHERE mark='�����';

UPDATE Exam_result
SET num_mark = 5
WHERE mark='³�����';


SELECT * FROM Exam_result