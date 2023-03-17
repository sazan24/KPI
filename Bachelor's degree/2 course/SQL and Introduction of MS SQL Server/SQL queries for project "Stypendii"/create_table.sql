DROP TABLE IF EXISTS Scholarship;

CREATE TABLE Scholarship (
  ID__scholarship INT PRIMARY KEY IDENTITY,
  ID__student INT FOREIGN KEY REFERENCES Student(ID__student) ON DELETE CASCADE,
  scholarship_amount FLOAT NOT NULL,  
);


INSERT INTO Scholarship(ID__student, scholarship_amount) 
  VALUES(1, 0), (2, 2910), (3, 2000), (4, 0), 
        (5, 2000), (6, 2000), (7, 2910), (8, 2910),
		(9, 0), (10, 2000), (11, 2000), (12, 0), 
		(13, 0), (14, 2910), (15, 2000), (16, 0);
