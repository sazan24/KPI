CREATE PROCEDURE [����� ������䳿 ��������] @group_name VARCHAR(5), @lastname VARCHAR(15), @firstname VARCHAR(15), @partonymic_name VARCHAR(15) 
AS
SELECT group_name AS '����� �����', 
       lastname '�������', 
	   firstname AS '�����',
	   patronymic_name AS '��-�������',
	   scholarship_amount AS '����� ������䳿'
FROM 
  Group_name JOIN Student
  ON Group_name.ID__group_name = Student.ID__group_name
  JOIN Scholarship
  ON Student.ID__student = Scholarship.ID__student
WHERE group_name = @group_name AND lastname = @lastname AND firstname = @firstname AND patronymic_name = @partonymic_name


EXEC [����� ������䳿 ��������] @group_name = '��-01', @lastname = '�����', @firstname = '�����', @partonymic_name = '���������';

EXEC [����� ������䳿 ��������] @group_name = '��-01', @lastname = 'ͳ���', @firstname = '���������', @partonymic_name = '����������';

EXEC [����� ������䳿 ��������] @group_name = '��-05', @lastname = '�������', @firstname = '�����', @partonymic_name = '�����';

EXEC [����� ������䳿 ��������] @group_name = 'Բ-02', @lastname = '��������', @firstname = '��������', @partonymic_name = '��������';
