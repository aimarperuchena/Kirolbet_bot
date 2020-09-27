import mysql.connector

dbServerName = "35.242.242.84"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"

mydb = mysql.connector.connect(
  host=dbServerName,
  user=dbUser,
  password=dbPassword,
  database=dbName
)

mycursor = mydb.cursor()
""" 
mycursor.execute("SELECT * FROM sport")

myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

sql = "INSERT INTO error (type, des) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowid, "record inserted.")