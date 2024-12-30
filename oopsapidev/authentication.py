from db_server import  Dbsc
from validation import Validation
import json
# from jwttoken import Jwttoken

class Auth_token(Validation):
    def __init__(self, host, dbname, user, password):
        super().__init__(host, dbname, user, password)  # Call the parent constructor
        # self.jwttoken = Jwttoken(host, dbname, user, password)  # Initialize jwttoken

    def get_user(self, token):
        response = self.validation_token(token)
        if response:
            get_q = '''
            SELECT username FROM edwin.users
            '''
            conn = self.dbsc.db_connection()
            cur = conn.cursor()
            cur.execute(get_q)
            response = cur.fetchall()
            j_res = self.json_data_transform(response)
            return j_res
        else:
            return {"message": "bad request"}

    def json_data_transform(self, response):  
        json_body = {'users': []}
        for i in response:
            json_body['users'].append(i[0])  
        return json.dumps(json_body)
