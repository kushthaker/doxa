from flask import request, jsonify
import jwt
from application.models import User
from application.initialize.config import Config
from functools import wraps

def token_required(f):
  @wraps(f)
  def _verify(*args, **kwargs):
    auth_headers = request.headers.get('Authorization', '').split()
    invalid_msg = {
      'Invalid token': ['Invalid token. Registration and / or authentication required']
    }
    expired_msg = {
      'Expired token': ['Expired token. Reauthentication required.']
    }
    if len(auth_headers) != 2:
      return jsonify(invalid_msg), 401

    try:
      token = auth_headers[1]
      data = jwt.decode(token, Config.APPLICATION_SECRET_KEY)
      user = User.query.filter_by(email=data['sub']).first()
      if not user:
        raise RuntimeError('User not found')
      return f(user, *args, **kwargs)
    except jwt.ExpiredSignatureError:
      return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError, Exception) as e:
      print(e)
      return jsonify(invalid_msg), 401

  return _verify
