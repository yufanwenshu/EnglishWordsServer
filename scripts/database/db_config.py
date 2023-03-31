HOSTNAME = "gz-cynosdbmysql-grp-pgr6w5y7.sql.tencentcdb.com"
DATABASE = 'EnglishWords'
PORT = 28996
USERNAME = 'root'
PASSWORD = 'Cwj010728'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

LOGIN_SQL_USERNAME = '''select * from user where username = "{}"'''
LOGIN_SQL_PASSWORD = '''select username, password, id, name, nickname, sex, \
    telephone, email, register_date, birthday, issuper from user \
    where binary username = "{}" and binary password = "{}"'''

if __name__ == "__main__":
    print(DB_URL)
    print(LOGIN_SQL)