from db import getAllNewsList
from flask import Flask
import json
app = Flask(__name__)

@app.route('/api/v1/getAllNews')
def getAllNews():
    allNewsList = getAllNewsList()
    jsonData = json.dumps(allNewsList, ensure_ascii=False)
    return jsonData

if __name__ == '__main__' :
    app.run()



