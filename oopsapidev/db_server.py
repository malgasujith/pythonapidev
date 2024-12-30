import psycopg2
from psycopg2 import Error


class Dbsc:
    def __init__(self,host,dbname,user,password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        super().__init__()
    def db_connection(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            print("Connected to the database successfully!")
            return conn
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise
    def user_schema(self):
        user_q = '''
        CREATE TABLE IF NOT EXISTS edwin.users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        mobile VARCHAR(50) UNIQUE NOT NULL,
        role VARCHAR(50) NOT NULL
        );
        '''

        secret_q = '''
        CREATE TABLE IF NOT EXISTS edwin.secret (
            id serial PRIMARY KEY,
            secret_key VARCHAR(60) UNIQUE NOT NULL
        );
        '''

        try:
            conn = self.db_connection()
            cur = conn.cursor()
            # Execute CREATE TABLE statements
            print("Creating tables...")
            cur.execute(user_q)
            cur.execute(secret_q)
            
            conn.commit()
            cur.close()
            conn.close()
            print("Tables created successfully (if they didn't already exist)!")
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            if conn:
                conn.close()
