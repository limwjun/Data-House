USE [maindb]
GO
/****** Object:  StoredProcedure [dbo].[SP_ETL_CREATE_LOGS]    Script Date: 2/10/2023 11:30:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[sp_etl_create_logs]   
  @BatchDate date,
  @MessageType nvarchar(5),
  @FunctionName varchar(255),
  @Messages NVARCHAR(max)
AS
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY

		IF @BatchDate IS NULL OR @BatchDate>GETDATE() 
		BEGIN
			SELECT @BatchDate=GETDATE()
		END

		WAITFOR DELAY '00:00:01'; -- 1 seconds delay

		insert into etl_msg_logs VALUES(@BatchDate, GETDATE(), @MessageType, @FunctionName, @Messages);
	END TRY

	BEGIN CATCH
		DECLARE @ERRMSG VARCHAR(255) = (select ERROR_MESSAGE());
		print @ERRMSG;

		exec [sp_etl_create_logs]  @batchdate, 'E', @FunctionName, @ERRMSG;
	END CATCH
END
