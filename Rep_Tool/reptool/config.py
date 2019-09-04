import os
# 'tx2hvHOecjI3LRhkpzZusA'
#SECRET_KEY = os.environ.get('SECRET_KEY')
#SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


# or MAIL_SERVER = 'localhost'
# MAIL_PORT = 25
# MAIL_USE_TLS = False
# MAIL_USE_SSL = False
# MAIL_DEBUG = app.debug
# MAIL_USERNAME = None
# MAIL_PASSWORD = None
# MAIL_DEFAULT_SENDER = None
# MAIL_MAX_EMAILS = None
# MAIL_SUPRESS_SEND = app.testing
# MAIL_ASCII_ATTACHMENTS = False

class Config:
    SECRET_KEY = 'tx2hvHOecjI3LRhkpzZusA'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    
    



   