USE [Інформаційна система відділу кадрів інституту]
GO


CREATE PROC [Видалити співробітника, що звільнився] @Nomer_pasporta VARCHAR(9)
AS
IF EXISTS (SELECT *     -- Перевірка на те, чи існує такий співробітник
		   FROM [Співробітники] 
		   WHERE [№ Паспорта] = @Nomer_pasporta)
    IF EXISTS (SELECT *     -- Видалити можна того співробітника, якому було підписано 'Наказ про звільнення'
               FROM [Наказ] 
               WHERE [№ Паспорта] = @Nomer_pasporta
    		         AND
    				 [Назва наказу] = 'Наказ про звільнення') 
        BEGIN
            DELETE FROM [Співробітники]
    	    WHERE [№ Паспорта] = @Nomer_pasporta
        END
    ELSE
        BEGIN
            RAISERROR('Не можна видалити запис, так як співробітника ще не звільнили', 0, 0)
        END
ELSE
    BEGIN
        RAISERROR('Не вірно введений номер паспорта, такого співробітника не існує', 0, 0)
    END
GO


CREATE PROC [Додати в базу нового співробітника] @PIB VARCHAR(50), @Birthdate DATE, @Nomer_pasporta VARCHAR(9), @IPN BIGINT, @Data_vydachi DATE, @Kym_vydano INT,
												 @Nomer_trudovoi INT, @Data_vydachi_trudovoi DATE,
						                         @Nomer_pensiinoho BIGINT, @Kafedra VARCHAR(100), @Stupin VARCHAR(30),

												   @ID__Nahorody INT, @Nahoroda VARCHAR(100), -- Може не бути, тому буде внесено на місці цих параметрів значення NULL
												 
												 @Nomer_nakazu INT, 
												 
												 @ID__Posady INT, @Posada VARCHAR(30)
AS
IF NOT EXISTS (SELECT *     -- Перевірка на те, чи можливо уже було внесено дані про співробітника
               FROM [Співробітники] 
               WHERE [№ Паспорта] = @Nomer_pasporta) 
    BEGIN
        INSERT INTO [Співробітники] ([ПІБ], [Дата народження], [№ Паспорта], [ІПН], [Дата видачі паспорта], [Ким видано паспорт],
							         [№ Трудової книжки], [Дата видачі трудової книжки], 
							         [№ Пенсійного посвідчення], [Кафедра], [Ступінь])
	    VALUES (@PIB, @Birthdate, @Nomer_pasporta, @IPN, @Data_vydachi, @Kym_vydano,
		  	    @Nomer_trudovoi, @Data_vydachi_trudovoi, 
			    @Nomer_pensiinoho, @Kafedra, @Stupin);

	    IF @ID__Nahorody != NULL AND @Nahoroda != NULL   -- Також потрібно ввести нагороду, якщо вона є
	        BEGIN
	            INSERT INTO [Перелік нагород] (ID__Нагороди, [№ Паспорта], [Нагорода])
		        VALUES (@ID__Nahorody, @Nomer_pasporta, @Nahoroda)
		    END

	    INSERT INTO [Наказ] ([№ Паспорта], [№ Наказу], [Назва наказу], [Дата видачі наказу])
	    VALUES (@Nomer_pasporta, @Nomer_nakazu, 'Наказ про зарахування', CAST( GETDATE() AS DATE)); -- Деякі значення будуть внесені по замовчуванню

	    INSERT INTO [Список посад] (ID__Посади, [№ Паспорта], [Посада])
        VALUES (@ID__Posady, @Nomer_pasporta, @Posada)
    END
ELSE
    BEGIN
        RAISERROR('Не можна добавити співробітника, який уже працює в інституті', 0, 0)
    END
GO


CREATE PROC [Увести дані нового контракту] @Nomer_pasporta VARCHAR(9), @Nomer_kontraktu INT, @Dystsyplina VARCHAR(50), @Data_ukladannia DATE, @Data_zakinchennia DATE
AS
IF EXISTS (SELECT *		-- Перевірка на те, чи існує такий співробітник
		   FROM [Співробітники] 
		   WHERE [№ Паспорта] = @Nomer_pasporta)
	IF EXISTS (SELECT *		-- Перевірка на те, чи цей співробітник може викладати
			   FROM [Викладачі] 
			   WHERE [№ Паспорта] = @Nomer_pasporta) 
		BEGIN
			INSERT INTO [Перелік дисциплін] ([№ Паспорта], [№ Контракту], [Дисципліна], [Дата укладання контракту], [Дата закінчення контракту])
			VALUES (@Nomer_pasporta, @Nomer_kontraktu, @Dystsyplina, @Data_ukladannia, @Data_zakinchennia)
		END
	ELSE
		BEGIN
			RAISERROR('Не вірно введений номер паспорта, такий співробітник не зможе викладати', 0, 0)
		END
ELSE
    BEGIN
        RAISERROR('Не вірно введений номер паспорта, такого співробітника не існує', 0, 0)
    END
GO


CREATE PROC [Змінити термін відпустки] @Nomer_pasporta VARCHAR(9), @Nomer_vidpustky INT, @Pochatok_vidpustky DATE, @Kinets_vidpustky DATE
AS
IF EXISTS (SELECT *		-- Перевірка на те, чи існує такий співробітник
		   FROM [Співробітники] 
		   WHERE [№ Паспорта] = @Nomer_pasporta) 
	IF EXISTS (SELECT *		                -- Перевірка на те, чи не закінився термін відпустки, адже змінювати можна лише дати майбутніх відпусток
		       FROM [Відпускні]             -- або ж дату закічнення відпустки (тобто можна подовжити поточну відпустку для співробітника)
		       WHERE [№ Відпустки] = @Nomer_vidpustky
				     AND
				     [№ Паспорта] = @Nomer_pasporta
					 AND
					 [Кінець відпустки] >= CAST( GETDATE() AS DATE)) 
		BEGIN
			UPDATE [Відпускні]
			SET [Початок відпустки] = @Pochatok_vidpustky, [Кінець відпустки] = @Kinets_vidpustky
			WHERE [№ Відпустки] = @Nomer_vidpustky
				  AND
				  [№ Паспорта] = @Nomer_pasporta
		END
	ELSE
	    BEGIN
			RAISERROR('Неможливо змінити дату відпустки, термін якої уже закінчився', 0, 0)
		END

ELSE
    BEGIN
        RAISERROR('Не вірно введений номер паспорта, такого співробітника не існує', 0, 0)
    END
GO


CREATE PROC [Змінити посаду певного співробітника] @Nomer_pasporta VARCHAR(9),
												 
												   @Nomer_nakazu INT, 
												 
												   @ID__Posady INT, @Posada VARCHAR(30)
AS
IF EXISTS (SELECT *     -- Перевірка на те, чи існує такий співробітник
		   FROM [Співробітники] 
		   WHERE [№ Паспорта] = @Nomer_pasporta) 
    BEGIN
	    INSERT INTO [Наказ] ([№ Паспорта], [№ Наказу], [Назва наказу], [Дата видачі наказу])
	    VALUES (@Nomer_pasporta, @Nomer_nakazu, 'Наказ про зміну посади', CAST( GETDATE() AS DATE)); -- Деякі значення будуть внесені по замовчуванню


	    /* Якщо співробітник був викладачем, то потрібно видалити його дані в таблиці [Викладачі] та [Перелік дисциплін]
           адже він більше не буде викладати, так як змінив посаду */ 
	    IF @ID__Posady = (SELECT ID__Посади    
		                  FROM [Список посад] 
		                  WHERE [№ Паспорта] = @Nomer_pasporta
							    AND
						        [Посада] = 'Викладач')     
	        BEGIN
				DELETE FROM [Викладачі] 
				WHERE [№ Паспорта] = @Nomer_pasporta  

				DELETE FROM [Перелік дисциплін]
				WHERE [№ Паспорта] = @Nomer_pasporta
            END			

	    UPDATE [Список посад]
	    SET [Посада] = @Posada
	    WHERE ID__Посади = @ID__Posady 
	          AND
	          [№ Паспорта] = @Nomer_pasporta
    END
ELSE 
    BEGIN
        RAISERROR('Не вірно введений номер паспорта, такого співробітника не існує', 0, 0)
    END
GO