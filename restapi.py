###Flask web server
from flask import Flask, request, url_for, redirect
from flask_restful import reqparse, abort, Api, Resource

###MySQL
import pymysql
from pymysql.cursors import DictCursor

###Config
from config import Config

###
from utils import access_database

###
import gc, time
from pprint import pprint

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():

    if request.method == 'POST':
        result = request.args.get('options')
        if result == 'index':

            cnx, cur = access_database()
            sql = """
            select * from temp_user
            """
            cur.execute(sql)
            results = cur.fetchall()
            # pprint(results)

            return url_for('result', options=result)

        elif result == 'type':

            return url_for('result', options=result)

        else:
            return 'Invalid Options : Please select another options ["index", "type"]'

        return result

    else:
        return 'Invalid Reqeusts'

    return '404'


@app.route('/result/<options>', methods=['GET'])
def result(options=None):

    if request.method == 'GET':
        if options == 'index':
            return '1'
        elif options == 'type':
            return '2'
        else:
            return 'Invalid Search options'


        return options

    else:
        return 'Invalid Reqeusts'

    return '404'




if __name__ == '__main__':
    app.run(debug=True)