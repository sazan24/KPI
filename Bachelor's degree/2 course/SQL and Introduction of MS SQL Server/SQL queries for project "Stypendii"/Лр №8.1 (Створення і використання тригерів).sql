CREATE TRIGGER [Видалити запис про результат здачі сесії, якщо стипендія = 0]
	ON Exam_result
	AFTER DELETE
AS
IF EXISTS (SELECT * 
           FROM deleted JOIN Scholarship 
           ON deleted.ID__student = Scholarship.ID__student
           WHERE Scholarship_amount != 0)
BEGIN
    RAISERROR('Не можна видалити результат', 0, 0)
    ROLLBACK TRAN 
END


DELETE FROM Exam_result
WHERE ID__student = 8

DELETE FROM Exam_result
WHERE ID__student = 12


SELECT * FROM Exam_result
