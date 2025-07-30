# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("28473509"))
    API_HASH = os.environ.get("f56218a21931d5f4ddcf0f0354256816")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOGS_CHANNEL = int(os.environ.get("-1002593438169"))
    BOT_OWNER = int(os.environ.get("5698467921"))
    MONGODB_URL = os.environ.get("mongodb+srv://rajraj101930:sXBnmE0VD7KVuFiw@cluster0.pfozrku.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Luckyjustx"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
