from application.run_server import application
import os

if __name__ == "__main__":
  if os.environ.get('IS_PRODUCTION'):
    print('running IS_PRODUCTION')
    application.run(use_reloader=False)
  else:
    print('running IS_DEBUG_MODE')
    application.run(debug=True, use_reloader=False)
