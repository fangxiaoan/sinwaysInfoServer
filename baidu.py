import requests
import re
import pymysql
def baidu(company):
        url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=' + company

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        res = requests.get(url, headers=headers).text



########正则提取规则
        p_href = '<h3 class="c-title">.*?<a href="(.*?)"'

        p_title = '<h3 class="c-title">.*?>(.*?)</a>'

        p_info = '<p class="c-author">(.*?)</p>'

        href = re.findall(p_href, res, re.S)

        title = re.findall(p_title, res, re.S)

        info = re.findall(p_info, res, re.S)

#######数据清洗
        source = []
        date = []
        db = pymysql.connect(host='192.168.8.176', port=3306, user='james', password='Fxa@880202', database='companynews')
        print('db--success')
        sql_select = 'SELECT news_title FROM news WHERE news_company = %s'
        curone = db.cursor()
        curone.execute(sql_select, company)
        data_all = curone.fetchall()
        print('fetchall success')
        curone.close()
        title_all=[]
        for j in range(len(data_all)):
                title_all.append(data_all[j][0])
        print('connect to mysql success')
        file1 = open('test.txt','a')
        for i in range(len(title)):
                title[i] = title[i].strip()
                title[i] = re.sub('<.*?>','',title[i])
                info[i] = re.sub('<.*?>','',info[i])

                source.append(info[i].split('&nbsp;&nbsp;')[0])
                date.append(info[i].split('&nbsp;&nbsp;')[1])
                source[i] = source[i].strip()
                date[i] = date[i].strip()

                print(str(i+1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')' )
                print(href[i])

                file1.write(str(i+1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')' + '\n')
                file1.write(href[i] + '\n')
                file1.write('--------------------------------------------------------------' + '\n' + '\n' )
                if title[i] not in title_all:
                        cur=db.cursor()
                        sql = 'INSERT INTO news(news_title,news_link,news_company,news_date,news_time) VALUES (%s,%s,%s,%s,%s)'
                        cur.execute(sql,(title[i],source[i],company,date[i],date[i]))
                        db.commit()
                        cur.close()
                        print("insert to mysql success")
        file1.close()
        db.close()
companys = ['南大光电','科蓝软件','中国平安','科大讯飞','招商证券']
for i in companys:
        try:
                baidu(i)
                print(i + "百度新闻爬取成功")
        except:
                print(i + '百度新闻爬取失败')

