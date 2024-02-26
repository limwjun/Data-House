**Part 2.1 - Data Collection**

The URL chosen to scrape data is item 1. Given that it is already a CSV link, the extraction process was fairly simple as no html parsing was needed.

**Part 2.2 - Transformation**

Prior to transformation, a quick check was done on the column names (to ensure SQL compatibility) and null / missing values was done. 

Upon checking, it is found that three columns had double quotation marks; which was renamed without quotation marks. There were no missing / null values in the data set.

For transformation, the following was done:-

1)  Split dataframe by year (in this case, three dataframes)
2)  Created new year column. In summary, there are three columns i.e. month, year and num (being the number of air travel).

The rationale behind the transformation is as follows:-

1)  The assumption is that the end users will want to perform analysis on the monthly air travel movement by year. The long term view is that new data will come in on a yearly basis and hence, expanding the data horizontally (adding new columns) based on the current data format may not be efficient for query lookup.
2)  The year column was created with the assumption that the end users may want to compare air travel movement in different years. For example, they may want to compare the number of air travel for Jan 1958 against Jan 1960. Having the year column will ease the analytical process.

**Part 2.3 Loading**

Leveraging on the pyodbc package, the three dataframes were loaded into three separate data tables in MSSQL.

**Part 2.4 Data Modelling**

Please refer to "Star Schema.png" for the star schema of the proposed data model. In summary, three data tables were created (segregated by years). The primary key for all three data tables is the Month column as it is a unique value. 

**Part 2.5 Visualization**

Leveraging on matplotlib, three visualisations were created, namely:

1) Number of air travel for Year 1958
2) Number of air travel for Year 1959
3) Number of air travel for Year 1960

Please refer to the respective png files for the visualisations.
