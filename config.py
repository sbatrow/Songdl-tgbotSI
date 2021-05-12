import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1613725086:AAFZH_fEG-x9XTHxVyada_Uhu8hL3X_gCoo", "")

    APP_ID = int(os.environ.get("2040626", 12345))

    API_HASH = os.environ.get("3b1dd5ee5b16901ab9f7d754217f040d", "")
