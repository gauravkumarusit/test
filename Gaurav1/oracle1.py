
import cx_Oracle
con = cx_Oracle.connect('system/bootey65@localhost')
print con.version
con.close()