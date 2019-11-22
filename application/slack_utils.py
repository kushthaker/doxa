from application import db
import slack

def create_user_from_api_user(slack_api_user):
  

def test_api_client(client):
  try:
    client.api_test()
  except SlackApiError:
    print('Client API test failed for token "%s"' % client.token)
    return False
  return True