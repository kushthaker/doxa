class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed' # will add later
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



# ---------------------------------------------------------------------------------------


# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

# SQLALCHEMY_DATABASE_URI = 'postgresql://pgmaster:postgres@doxa-database-staging.c8pjbrdeia2z.us-east-1.rds.amazonaws.com:5432'

# # Uncomment the line below if you want to work with a local DB
# #SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# SQLALCHEMY_POOL_RECYCLE = 3600

# WTF_CSRF_ENABLED = True
# SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'