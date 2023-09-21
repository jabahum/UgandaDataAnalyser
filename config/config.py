class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///efris.db"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "JWT-SECRET"
    SECRET_KEY = "SECRET-KEY"
    SECURITY_PASSWORD_SALT = "SECRET-KEY-PASSWORD"
    MAIL_DEFAULT_SENDER = ""
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = "465"
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    SERVER_URL = "https://mediator-api-staging.health.go.ug/fhir/Patient?_total=accurate&_tag:not=5c827da5-4858-4f3d-a50c-62ece001efea&_count="


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///efris.db"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "JWT-SECRET"
    SECRET_KEY = "SECRET-KEY"
    SECURITY_PASSWORD_SALT = "SECRET-KEY-PASSWORD"
    MAIL_DEFAULT_SENDER = ""
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = "465"
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    SERVER_URL = "https://mediator-api-staging.health.go.ug/fhir/Patient?_total=accurate&_tag:not=5c827da5-4858-4f3d-a50c-62ece001efea&_count="
