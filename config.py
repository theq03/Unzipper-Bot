# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("2572163"))
    API_HASH = os.environ.get("deede80ddff7842db6c90b5715635142")
    BOT_TOKEN = os.environ.get("5896556129:AAFZHjNvmG1eq4VVO45ThhjUZdMKk0gh9mM")
    LOGS_CHANNEL = int(os.environ.get("-1001623260624"))
    BOT_OWNER = int(os.environ.get("1292898087"))
    MONGODB_URL = os.environ.get("mongodb+srv://GDriveQbot:GDriveQbot@cluster0.2b9k6q5.mongodb.net/?retryWrites=true&w=majority")
    # Optional
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN")
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
