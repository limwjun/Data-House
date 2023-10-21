USE [maindb]
GO
/****** Object:  StoredProcedure [dbo].[SP_ETL_LOAD_MINIPORT]    Script Date: 2/10/2023 5:06:38 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_test]

@batchdate date,
@isDebug varchar(1) = 'N',
@inputstr varchar(255)

AS
BEGIN

DECLARE @FunctionName varchar(255) = (SELECT object_name(@@PROCID));
DECLARE @msg varchar(500);
DECLARE @ERRMSG VARCHAR(255);

BEGIN TRY

if @isDebug <> 'Y'
begin
set @Msg = 'Start - sp test';
exec [sp_etl_create_logs]  @batchdate, 'I',@FunctionName , @Msg;
end

	execute(@inputstr)

if @isDebug <> 'Y'
begin
set @msg = 'End - sp test';
exec [sp_etl_create_logs]  @batchdate, 'I', @FunctionName , @msg;
end

END TRY

BEGIN CATCH

set @ERRMSG = (select ERROR_MESSAGE());
exec [sp_etl_create_logs]  @batchdate, 'E', @FunctionName, @ERRMSG;

END CATCH
	
END