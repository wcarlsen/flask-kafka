class Config:
    PGHOST = "localhost"
    PGUSER = "postgres"
    PGPASSWD="p"
    PGDB = PGUSER
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=PGUSER,pw=PGPASSWD,url=PGHOST,db=PGDB)
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {"default": Config}
