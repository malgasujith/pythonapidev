import bcrypt
from psycopg2 import Binary
from db_server import Dbsc
from validation import Validation
from regibase import Reg_base

class reg_service(Reg_base):
    def __init__(self, host, dbname, user, password):
        self.dbsc = Dbsc(host, dbname, user, password)
        self.validation = Validation(host, dbname, user, password)  

    def has_value(self, password):
        res = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return res

    def user_registration(self, request, count: int = 0):
        print(request)
        user_response = self.validation.validate_user(request['username'])
        pass_response = self.validation.password_val(request['password'])
        if user_response and not pass_response:
            return {"message": "User already exists and password is not valid. Please try again."}
        else:
            hash_password = self.has_value(request['password'])
            print(hash_password)
            user_q = '''
            INSERT INTO edwin.users (username, password, email, mobile, role) VALUES (%s, %s, %s, %s, %s)
            '''
            values = (
                request['username'], Binary(hash_password),
                request['email'], request['mobile'], request['role']
            )
            conn = self.dbsc.db_connection()
            cur = conn.cursor()
            cur.execute(user_q, values)
            conn.commit()
            cur.close()
            conn.close()
            return {'message': "Registration is successful"}
