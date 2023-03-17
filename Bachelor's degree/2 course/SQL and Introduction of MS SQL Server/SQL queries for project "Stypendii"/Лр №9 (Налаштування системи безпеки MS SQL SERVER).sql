CREATE USER Bill WITHOUT LOGIN;

ALTER ROLE db_securityadmin ADD MEMBER Bill;

GRANT EXECUTE ON [����� ������䳿 ��������] TO Bill;

REVOKE EXECUTE ON [����� ������䳿 ��������] FROM Bill;


/* 1. �������� ������-���� ���� ����� */
CREATE MASTER KEY ENCRYPTION BY PASSWORD = '23112021'

/* 2. �������� ����������. ���������� ���������� SQL Server */
CREATE CERTIFICATE Scholarship_Sertificate
WITH SUBJECT = 'Protect Data'

/* 3. ��������� ������������ ����� */
CREATE SYMMETRIC KEY Symmetric_Key
WITH ALGORITHM = AES_128
ENCRYPTION BY CERTIFICATE Scholarship_Sertificate;

/* 4. �������� ������� ��� ��������� ����������� ���������� �����, ��� varbinary */
ALTER TABLE Scholarship
ADD Encrypted_scholarship_amount varbinary(MAX) NULL

/* 5. ���������� ������� ������� */
-- ³������ ����������� ����, ��� �����������
OPEN SYMMETRIC KEY Symmetric_key
DECRYPTION BY CERTIFICATE Scholarship_Sertificate;
UPDATE Scholarship
SET Encrypted_scholarship_amount = EncryptByKey(Key_GUID('Symmetric_key'), scholarship_amount)
FROM Scholarship;
-- ������� ����������� ����
CLOSE SYMMETRIC KEY Symmetric_key;

SELECT * FROM Scholarship