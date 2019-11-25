from application import application
import os

if __name__ == "__main__":
  if os.environ.get('IS_PRODUCTION'):
    application.run(use_reloader=False)
  else:
    application.run(debug=True, use_reloader=False)
