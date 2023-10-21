USE [maindb]
GO

/****** Object:  Table [dbo].[etl_msg_logs]    Script Date: 2/10/2023 5:08:32 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO
IF OBJECT_ID('dbo.etl_msg_logs', 'U') IS NOT NULL
DROP TABLE dbo.etl_msg_logs
GO
CREATE TABLE [dbo].[etl_msg_logs](
	[BatchDate] [date] NULL,
	[LogTime] [datetime] NULL,
	[MessageType] [char](5) NULL,
	[FunctionName] [nvarchar](255) NULL,
	[Message] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


