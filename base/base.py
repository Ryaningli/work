class Modifier:
    def __init__(self, db):
        self.db = db

    # 获取token
    def base_get_token(self, username):
        sql = 'SELECT user_token FROM bsn_user WHERE user_phone="{}"'.format(username)
        cursor = self.db.cursor()

    # 获取服务id
    def base_get_app_id(self, app_name):
        pass

    # 改钱
    def base_mod_money(self, username):
        pass

    # 生成流量订单
    def base_make_flow_order(self, app_id):
        pass

    # 生成续费订单
    def base_make_renew_order(self, app_id):
        pass
