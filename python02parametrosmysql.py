import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='getafe',passwd='mysql',db='HOSPITAL')

sql= "select * from EMP where SALARIO >= %s"
cursor = connection.cursor()
print("Introduzca un salario")
salario= int(input())
cursor.execute(sql,(salario,))
for row in cursor:
    print(f"Apellido {row[1]}, oficio: {row[2]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Finde Programa")
