USE [������������ ������� ����� ����� ���������]
GO


CREATE PROC [�������� �����������, �� ���������] @Nomer_pasporta VARCHAR(9)
AS
IF EXISTS (SELECT *     -- �������� �� ��, �� ���� ����� ����������
		   FROM [�����������] 
		   WHERE [� ��������] = @Nomer_pasporta)
    IF EXISTS (SELECT *     -- �������� ����� ���� �����������, ����� ���� �������� '����� ��� ���������'
               FROM [�����] 
               WHERE [� ��������] = @Nomer_pasporta
    		         AND
    				 [����� ������] = '����� ��� ���������') 
        BEGIN
            DELETE FROM [�����������]
    	    WHERE [� ��������] = @Nomer_pasporta
        END
    ELSE
        BEGIN
            RAISERROR('�� ����� �������� �����, ��� �� ����������� �� �� ��������', 0, 0)
        END
ELSE
    BEGIN
        RAISERROR('�� ���� �������� ����� ��������, ������ ����������� �� ����', 0, 0)
    END
GO


CREATE PROC [������ � ���� ������ �����������] @PIB VARCHAR(50), @Birthdate DATE, @Nomer_pasporta VARCHAR(9), @IPN BIGINT, @Data_vydachi DATE, @Kym_vydano INT,
												 @Nomer_trudovoi INT, @Data_vydachi_trudovoi DATE,
						                         @Nomer_pensiinoho BIGINT, @Kafedra VARCHAR(100), @Stupin VARCHAR(30),

												   @ID__Nahorody INT, @Nahoroda VARCHAR(100), -- ���� �� ����, ���� ���� ������� �� ���� ��� ��������� �������� NULL
												 
												 @Nomer_nakazu INT, 
												 
												 @ID__Posady INT, @Posada VARCHAR(30)
AS
IF NOT EXISTS (SELECT *     -- �������� �� ��, �� ������� ��� ���� ������� ��� ��� �����������
               FROM [�����������] 
               WHERE [� ��������] = @Nomer_pasporta) 
    BEGIN
        INSERT INTO [�����������] ([ϲ�], [���� ����������], [� ��������], [���], [���� ������ ��������], [��� ������ �������],
							         [� ������� ������], [���� ������ ������� ������], 
							         [� ��������� ����������], [�������], [������])
	    VALUES (@PIB, @Birthdate, @Nomer_pasporta, @IPN, @Data_vydachi, @Kym_vydano,
		  	    @Nomer_trudovoi, @Data_vydachi_trudovoi, 
			    @Nomer_pensiinoho, @Kafedra, @Stupin);

	    IF @ID__Nahorody != NULL AND @Nahoroda != NULL   -- ����� ������� ������ ��������, ���� ���� �
	        BEGIN
	            INSERT INTO [������ �������] (ID__��������, [� ��������], [��������])
		        VALUES (@ID__Nahorody, @Nomer_pasporta, @Nahoroda)
		    END

	    INSERT INTO [�����] ([� ��������], [� ������], [����� ������], [���� ������ ������])
	    VALUES (@Nomer_pasporta, @Nomer_nakazu, '����� ��� �����������', CAST( GETDATE() AS DATE)); -- ���� �������� ������ ������ �� ������������

	    INSERT INTO [������ �����] (ID__������, [� ��������], [������])
        VALUES (@ID__Posady, @Nomer_pasporta, @Posada)
    END
ELSE
    BEGIN
        RAISERROR('�� ����� �������� �����������, ���� ��� ������ � ��������', 0, 0)
    END
GO


CREATE PROC [������ ��� ������ ���������] @Nomer_pasporta VARCHAR(9), @Nomer_kontraktu INT, @Dystsyplina VARCHAR(50), @Data_ukladannia DATE, @Data_zakinchennia DATE
AS
IF EXISTS (SELECT *		-- �������� �� ��, �� ���� ����� ����������
		   FROM [�����������] 
		   WHERE [� ��������] = @Nomer_pasporta)
	IF EXISTS (SELECT *		-- �������� �� ��, �� ��� ���������� ���� ���������
			   FROM [���������] 
			   WHERE [� ��������] = @Nomer_pasporta) 
		BEGIN
			INSERT INTO [������ ��������] ([� ��������], [� ���������], [���������], [���� ��������� ���������], [���� ��������� ���������])
			VALUES (@Nomer_pasporta, @Nomer_kontraktu, @Dystsyplina, @Data_ukladannia, @Data_zakinchennia)
		END
	ELSE
		BEGIN
			RAISERROR('�� ���� �������� ����� ��������, ����� ���������� �� ����� ���������', 0, 0)
		END
ELSE
    BEGIN
        RAISERROR('�� ���� �������� ����� ��������, ������ ����������� �� ����', 0, 0)
    END
GO


CREATE PROC [������ ����� ��������] @Nomer_pasporta VARCHAR(9), @Nomer_vidpustky INT, @Pochatok_vidpustky DATE, @Kinets_vidpustky DATE
AS
IF EXISTS (SELECT *		-- �������� �� ��, �� ���� ����� ����������
		   FROM [�����������] 
		   WHERE [� ��������] = @Nomer_pasporta) 
	IF EXISTS (SELECT *		                -- �������� �� ��, �� �� �������� ����� ��������, ���� �������� ����� ���� ���� �������� ��������
		       FROM [³������]             -- ��� � ���� ��������� �������� (����� ����� ��������� ������� �������� ��� �����������)
		       WHERE [� ³�������] = @Nomer_vidpustky
				     AND
				     [� ��������] = @Nomer_pasporta
					 AND
					 [ʳ���� ��������] >= CAST( GETDATE() AS DATE)) 
		BEGIN
			UPDATE [³������]
			SET [������� ��������] = @Pochatok_vidpustky, [ʳ���� ��������] = @Kinets_vidpustky
			WHERE [� ³�������] = @Nomer_vidpustky
				  AND
				  [� ��������] = @Nomer_pasporta
		END
	ELSE
	    BEGIN
			RAISERROR('��������� ������ ���� ��������, ����� ��� ��� ���������', 0, 0)
		END

ELSE
    BEGIN
        RAISERROR('�� ���� �������� ����� ��������, ������ ����������� �� ����', 0, 0)
    END
GO


CREATE PROC [������ ������ ������� �����������] @Nomer_pasporta VARCHAR(9),
												 
												   @Nomer_nakazu INT, 
												 
												   @ID__Posady INT, @Posada VARCHAR(30)
AS
IF EXISTS (SELECT *     -- �������� �� ��, �� ���� ����� ����������
		   FROM [�����������] 
		   WHERE [� ��������] = @Nomer_pasporta) 
    BEGIN
	    INSERT INTO [�����] ([� ��������], [� ������], [����� ������], [���� ������ ������])
	    VALUES (@Nomer_pasporta, @Nomer_nakazu, '����� ��� ���� ������', CAST( GETDATE() AS DATE)); -- ���� �������� ������ ������ �� ������������


	    /* ���� ���������� ��� ����������, �� ������� �������� ���� ��� � ������� [���������] �� [������ ��������]
           ���� �� ����� �� ���� ���������, ��� �� ����� ������ */ 
	    IF @ID__Posady = (SELECT ID__������    
		                  FROM [������ �����] 
		                  WHERE [� ��������] = @Nomer_pasporta
							    AND
						        [������] = '��������')     
	        BEGIN
				DELETE FROM [���������] 
				WHERE [� ��������] = @Nomer_pasporta  

				DELETE FROM [������ ��������]
				WHERE [� ��������] = @Nomer_pasporta
            END			

	    UPDATE [������ �����]
	    SET [������] = @Posada
	    WHERE ID__������ = @ID__Posady 
	          AND
	          [� ��������] = @Nomer_pasporta
    END
ELSE 
    BEGIN
        RAISERROR('�� ���� �������� ����� ��������, ������ ����������� �� ����', 0, 0)
    END
GO