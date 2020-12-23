import pymysql


# 打开数据库连接
db = pymysql.connect('120.78.138.215', 'root', '12345678', 'sc_bsn_test')

# 创建游标对象
cursor = db.cursor()

# 查询
sql = 'SELECT user_token FROM bsn_user WHERE user_phone="18815596963"'
# cursor.execute('SELECT * FROM bsn_user WHERE user_phone="18815596963"')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 获取数据
data = cursor.fetchone()

# 打印数据
print(data)

# 关闭数据库连接
db.close()