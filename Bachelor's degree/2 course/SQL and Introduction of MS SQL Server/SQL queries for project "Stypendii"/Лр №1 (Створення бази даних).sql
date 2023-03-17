DROP TABLE IF EXISTS Student, Group_name, Exam_result;

CREATE TABLE Group_name (
  ID__group_name INT PRIMARY KEY IDENTITY, 
  group_name VARCHAR(5) UNIQUE NOT NULL,
);
CREATE TABLE Student (
  ID__student INT PRIMARY KEY IDENTITY, 
  ID__group_name INT FOREIGN KEY REFERENCES Group_name(ID__group_name) ON DELETE CASCADE, 
  lastname VARCHAR(15) NOT NULL, 
  firstname VARCHAR(15) NOT NULL, 
  patronymic_name VARCHAR(15) NOT NULL, 
  CONSTRAINT StudentPrimary UNIQUE (lastname, firstname, patronymic_name),
);
CREATE TABLE Exam_result (
  ID__mark INT PRIMARY KEY IDENTITY,
  ID__student INT NOT NULL, 
  mark VARCHAR(10) NOT NULL,
  CONSTRAINT Exam_resultForeign FOREIGN KEY (ID__student) REFERENCES Student (ID__student) ON DELETE CASCADE,
  CONSTRAINT Exam_markCheck CHECK(mark IN ('�� ����', '���������', '�����', '³�����')),
);
