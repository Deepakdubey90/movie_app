import os
import json
import dj_database_url

SECRET_KEY = 'wa9g_mf%mrairp7#c#&&5pt0y4+5pk2skbizk!$c5km5lbzs^&'

DEBUG = False

connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}

ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
