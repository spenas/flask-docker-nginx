from appl import create_app

app = create_app()

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', debug=ENVIRONMENT_DEBUG, port=ENVIRONMENT_PORT)