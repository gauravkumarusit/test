import mysql.connector
conn=mysql.connector.connect(host='localhost',database='world',user='root',password='bootey65')
if conn.is_connected():
    print "connected to mysql database :-)"
    cursor=conn.cursor()
    cursor.execute("select * from pet;")
    row=cursor.fetchall()
    print row
    #cursor.close()
    conn.close()
    