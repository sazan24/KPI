CREATE PROCEDURE [Розмір стипендії студента] @group_name VARCHAR(5), @lastname VARCHAR(15), @firstname VARCHAR(15), @partonymic_name VARCHAR(15) 
AS
SELECT group_name AS 'Назва групи', 
       lastname 'Прізвище', 
	   firstname AS 'Імена',
	   patronymic_name AS 'По-батькові',
	   scholarship_amount AS 'Розмір стипендії'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Scholarship
  ON Student.ID__student = Scholarship.ID__student
WHERE group_name = @group_name AND lastname = @lastname AND firstname = @firstname AND patronymic_name = @partonymic_name


EXEC [Розмір стипендії студента] @group_name = 'ФБ-01', @lastname = 'Сахній', @firstname = 'Назар', @partonymic_name = 'Романович';

EXEC [Розмір стипендії студента] @group_name = 'ФЕ-01', @lastname = 'Нікітін', @firstname = 'Костянтин', @partonymic_name = 'Георгійович';

EXEC [Розмір стипендії студента] @group_name = 'ФБ-05', @lastname = 'Раменра', @firstname = 'Мурат', @partonymic_name = 'Саміль';

EXEC [Розмір стипендії студента] @group_name = 'ФІ-02', @lastname = 'Єрмолатій', @firstname = 'Валентин', @partonymic_name = 'Ігорович';
