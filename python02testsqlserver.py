import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;database=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
print("Funciona SQL Server")