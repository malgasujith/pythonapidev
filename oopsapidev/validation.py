import re
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError
from db_server import Dbsc
from jwttoken import Jwttoken

class Validation(Jwttoken):
    def __init__(self, host, dbname, user, password):
        self.dbsc = Dbsc(host, dbname, user, password)
        # self.jwttoken = Jwttoken(host, dbname, user, password)


    def validate_user(self, user: str) -> bool:
        try:
            user_q = '''
            SELECT username FROM edwin.users WHERE username = %s
            '''
            conn = self.dbsc.db_connection()
            cur = conn.cursor()
            cur.execute(user_q, (user,))
            result = cur.fetchone()
            return result is not None
        except Exception as e:
            print(f"Error validating user: {e}")
            return False

    def password_val(self, password: str) -> bool:
        pattern = r'^[a-zA-Z0-9]{8,}$'
        return bool(re.match(pattern, password))

    def validation_token(self, token):
        print(f"Decoding token: {token}")  # Log the token for debugging
        secret = self.get_secret()
        try:
            token_encode = jwt.decode(token, secret, algorithms=['HS256'])
            return token_encode
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError as e:
            raise ValueError(f"Invalid token: {str(e)}")