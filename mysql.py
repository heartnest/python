import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")


try: 
	query = "INSERT INTO components (code, name, description, category_id, parameter_1) VALUES (%s, %s, %s, %s, %s)"
	val = (code, description, description, categ, param_1)
	mycursor.execute(query,val)
	mydb.commit()
except TypeError as e:
	print(e)
	mydb.rollback()


print(mycursor.rowcount, "record inserted.")