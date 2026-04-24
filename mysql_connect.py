import mysql.connector

mydb = mysql.connector.connect(
  host="host.docker.internal",  # 宿主机
  user="root",
  password="root",
  database="default"
)
print(mydb)

# 获取游标
mycursor = mydb.cursor()

# 显示数据库
mycursor.execute("SHOW DATABASES")

# 输出结果
print("✅ 连接成功！数据库列表：")
for db in mycursor:
  print(db)