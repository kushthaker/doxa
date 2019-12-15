import os

class Config:
  # basic stuff
  APPLICATION_SECRET_KEY = '7a273729d601733097ead8f655a410eb'

  # Slack API keys
  SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID') # stored in EB config
  SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET') # stored in EB config

  GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') # stored in EB config
  GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') # stored in EB config

  # Google OAuth2 throws insecure transport error without https, this is temp workaround.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  CORS_HEADERS = 'Content-Type'
  # database stuff
  LOCAL_PG_URL = 'postgresql://localhost/doxa_dev'
  postgres_url = os.environ.get('AWS_RDS_URL')
  if postgres_url != None:
    print('USING VARIABLE %s' % postgres_url)
    SQLALCHEMY_DATABASE_URI = postgres_url
  else:
    print('USING VARIABLE LOCAL')
    SQLALCHEMY_DATABASE_URI = LOCAL_PG_URL

  # gets rid of annoying message when starting app
  sqlalchemy_tracking_notifications = not os.environ.get('IS_PRODUCTION')
  if sqlalchemy_tracking_notifications:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
  else:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
