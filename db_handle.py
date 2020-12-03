#数据库操作

import pymysql

def update_key(code):
     # 建立数据库连接
    db=pymysql.connect(
        host='',
        port=3306,
        user='',
        password='',
        db='',
        charset='utf8'
    )
    sql = f"update payconfig set SandboxKey = '{code}' where `Name` = 'test1' or `Name` = 'test2'"
    #使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    #使用execute()方法执行SQL语句
    cursor.execute(sql)
     # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    db.commit()

    # 关闭cursor对象
    cursor.close()
    # 关闭connection对象
    db.close()
    

