import pymysql
user = 'admin'
password = 'Fxa@880202'
host = '47.112.213.237'
port = 3306
database = 'companynews'

def getAllNewsList():
    db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = db.cursor()
    sql = 'select * from news'
    cursor.execute(sql)

    allNews = cursor.fetchall()
    allNewsList=[]
    for i in range(len(allNews)):
        news = {}
        news['id'] = allNews[i][0]
        news['news_title'] = allNews[i][1]
        news['news_link'] = allNews[i][2]
        news['news_company'] = allNews[i][3]
        news['news_date'] = allNews[i][4]
        news['news_time'] = allNews[i][5]
        allNewsList.append(news)

    cursor.close()
    db.close()
    return allNewsList
