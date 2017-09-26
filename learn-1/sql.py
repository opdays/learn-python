import mysql.connector

config = {
    "host":"192.168.53.132",
    "user":"admin",
    "password":"yangyang123",
    "charset":"utf8",
    "database":"asset_cmdb",
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
sql = "desc t_asset"

cursor.execute(sql)

values = cursor.fetchall()

print(values)
for v in values:
    print(v[0])
