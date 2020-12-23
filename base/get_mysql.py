import pymysql


class GetMysql:
    db = None

    # 获取MySQL连接游标
    @classmethod
    def get_mysql(cls):
        if cls.db is None:
            cls.db = pymysql.connect('120.78.138.215', 'root', '12345678', 'sc_bsn_test')

        return cls.db

    # 关闭mysql连接
    @classmethod
    def close_mysql(cls):
        if cls.db:
            cls.db.close()
            cls.db = None

