###MySQL
import pymysql
from pymysql.cursors import DictCursor

###Config
from config import Config


db = Config['database']


def access_database():
    cnx = pymysql.connect(
        user=db['user'],
        password=db['password'],
        host=db['host'],
        database=db['database'],
        charset='utf8mb4'
    )
    cur = cnx.cursor(DictCursor)
    return cnx, cur

