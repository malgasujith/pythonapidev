import jwt
from datetime import datetime, timezone, timedelta
from db_server import  Dbsc

class Jwttoken(Dbsc):
    def __init__(self, host, dbname, user, password):
        self.dbsc = Dbsc(host, dbname, user, password)
        # self.validation = Validation(host, dbname, user, password)  

    def get_secret(self):
        user_q = '''
        SELECT secret_key FROM edwin.secret
        '''
        conn = self.dbsc.db_connection()
        cur = conn.cursor()
        cur.execute(user_q)
        response_secret = cur.fetchone()[0]
        cur.close()
        conn.close()
        return response_secret

    def creat_token(self,body):
        
        expire_create = datetime.now(timezone.utc) + timedelta(days=body['expire'])
        body = {
            'username': body['username'],
            'role': body['role'],
            'exp': expire_create.timestamp()  
        }
        secret = self.get_secret()
        token = jwt.encode(body, secret, algorithm="HS256")
        return token
