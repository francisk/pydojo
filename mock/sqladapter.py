from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor
import MySQLdb


class Adapter(object):
    """
    MySqldb adapter
    """
    #connection pool
    __pool = None
    
    def __init__(self):
        self._conn = Adapter.__get_conn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __get_conn():
        if Adapter.__pool is None:
            __pool = PooledDB(creator=MySQLdb,
                              mincached=1,
                              maxcached=20,
                              host="localhost",
                              port=3306,
                              user="root",
                              passwd="root",
                              db="game_dev",
                              charset="utf8",
                              cursorclass=DictCursor)
            return __pool.connection()
    @staticmethod
    def __query(sql,param=None):
        pass


    def get_all(self,table_name):
        sql="select * from %s" %(table_name)
        count = self._cursor.execute(sql)
        if count > 0:
            result = list(self._cursor.fetchall())
        else:
            result = False
        return result
        
    def get_by_id(self,table_name,id):
        sql = "select * from %s where Id= %s" %(table_name,id)
        count = self._cursor.execute(sql)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

