from etrade.models import db
from etrade import createApp


def createDB():
    db.create_all(app=createApp())