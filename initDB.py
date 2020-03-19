import pymysql
""" 
1，连接到aliyun数据库  47.112.213.237：3306
2，建立游标
3，创建表
4，
"""
path = ''
user = 'admin'
password = 'Fxa@880202'
host = '47.112.213.237'
port = 3306
database = 'companynews'
def create_table():
    db = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS news')

    sql = """CREATE TABLE news(
            id INT NOT NULL AUTO_INCREMENT primary key,
            news_title char(40),
            news_from char(40),
            news_company char(30),
            news_link char(20),
            news_date char(20)
             )"""

    try:
        cursor.execute(sql)
        print("success to create the table news")
    except Exception as e:
        print('failed to create the table news, case'%e)
    finally:
        cursor.close()
        db.close()
def main():
    create_table()

if __name__ == '__main__':
    main()