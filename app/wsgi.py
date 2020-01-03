from appl import create_app
import os
application = create_app()

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', debug=ENVIRONMENT_DEBUG, port=ENVIRONMENT_PORT)