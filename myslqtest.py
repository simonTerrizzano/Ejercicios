import pymyslq

db = pymyslq.connect("sql10.freemysqlhosting.net","sql10475112","iE5xceSrGA","sql10475112")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version: {0} ".format(data)) 