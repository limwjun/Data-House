# 2.1 - Part 1: Data Collection

import requests

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
r = requests.get(url)
with open('airtravel.csv', 'wb') as f:
            # Write the contents of the response to the file
            f.write(r.content)
        
# 2.2 Part 2 : Transformation 
# For the data collected, provide and perform any possible transformation processes, and explain why such transformation needed.

import pandas as pd
import numpy as np

df = pd.read_csv('airtravel.csv', delimiter=',')
print(df.head())

# Check for null / missing values
print(df.isna().sum())


# Remove double quotation marks from column names
df = df.rename(columns={' "1958"':'1958',' "1959"':'1959',' "1960"':'1960'})
print(df.head())


# Create three dataframes to segregate yearly data
df_1958 =  df[['Month','1958']].rename(columns={'1958':'Num'})
df_1958['Year'] = 1958

df_1959 =  df[['Month','1959']].rename(columns={'1959':'Num'})
df_1959['Year'] = 1959

df_1960 =  df[['Month','1960']].rename(columns={'1960':'Num'})
df_1960['Year'] = 1960

# 2.3 Part 3 : Loading
import pyodbc

server = 'localhost,1433' 
database = 'Work' 
username = '' 
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';TrustServerCertificate=yes')
cursor = cnxn.cursor()
cursor.execute("""IF OBJECT_ID('AirTravel1958', 'U') IS NULL CREATE TABLE AirTravel1958(Year int NOT NULL, Month varchar(3) NOT NULL, [Num] int NOT NULL,PRIMARY KEY (Month))""")
cursor.execute("""IF OBJECT_ID('AirTravel1959', 'U') IS NULL CREATE TABLE AirTravel1959(Year int NOT NULL, Month varchar(3) NOT NULL, [Num] int NOT NULL,PRIMARY KEY (Month))""")
cursor.execute("""IF OBJECT_ID('AirTravel1960', 'U') IS NULL CREATE TABLE AirTravel1960(Year int NOT NULL, Month varchar(3) NOT NULL, [Num] int NOT NULL,PRIMARY KEY (Month))""")

# Insert data into SQL Server:
for index, row in df_1958.iterrows():
     cursor.execute('INSERT INTO AirTravel1958 (Year, Month, Num) values(?,?,?)', row.Year, row.Month, row.Num)

for index, row in df_1959.iterrows():
     cursor.execute('INSERT INTO AirTravel1959 (Year, Month, Num) values(?,?,?)', row.Year, row.Month, row.Num)

for index, row in df_1960.iterrows():
     cursor.execute('INSERT INTO AirTravel1960 (Year, Month, Num) values(?,?,?)', row.Year, row.Month, row.Num)

cnxn.commit()
cursor.close()

# 2.5 Part 5 - Visualization

import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(df_1958,x = 'Month', y = 'Num')
plt.title('Number of air travel for Year 1958')
plt.show()

sns.barplot(df_1959,x = 'Month', y = 'Num')
plt.title('Number of air travel for Year 1959')
plt.show()

sns.barplot(df_1960,x = 'Month', y = 'Num')
plt.title('Number of air travel for Year 1960')
plt.show()
