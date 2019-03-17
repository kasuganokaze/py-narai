import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='12345Aa.',
                       database='kaze')
cur = conn.cursor()
cur.execute("select * from sys_user")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
