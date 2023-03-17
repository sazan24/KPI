CREATE USER Bill WITHOUT LOGIN;

ALTER ROLE db_securityadmin ADD MEMBER Bill;

GRANT EXECUTE ON [Розмір стипендії студента] TO Bill;

REVOKE EXECUTE ON [Розмір стипендії студента] FROM Bill;


/* 1. Створити мастер-ключ бази даних */
CREATE MASTER KEY ENCRYPTION BY PASSWORD = '23112021'

/* 2. Створити сертификат. Сертификат підписується SQL Server */
CREATE CERTIFICATE Scholarship_Sertificate
WITH SUBJECT = 'Protect Data'

/* 3. Створення симетричного ключа */
CREATE SYMMETRIC KEY Symmetric_Key
WITH ALGORITHM = AES_128
ENCRYPTION BY CERTIFICATE Scholarship_Sertificate;

/* 4. Додавамо колонку для зберігання зашифрованої інформації даних, тип varbinary */
ALTER TABLE Scholarship
ADD Encrypted_scholarship_amount varbinary(MAX) NULL

/* 5. Шифрування колонки таблиці */
-- Відкриємо симетричний ключ, щоб використати
OPEN SYMMETRIC KEY Symmetric_key
DECRYPTION BY CERTIFICATE Scholarship_Sertificate;
UPDATE Scholarship
SET Encrypted_scholarship_amount = EncryptByKey(Key_GUID('Symmetric_key'), scholarship_amount)
FROM Scholarship;
-- Закриємо симетричний ключ
CLOSE SYMMETRIC KEY Symmetric_key;

SELECT * FROM Scholarship