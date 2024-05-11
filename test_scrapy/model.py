"""
Model for storing data
---------------------
This model is using for data storing and it connects to mongodb.
When we import this module to other module, it will automaticall
connect to the database using the `ORM` framework.
"""

from datetime import datetime
from test_scrapy import settings
from mongoengine import (
    connect,
    Document,
    StringField,
    BooleanField,
    ListField,
    DateTimeField,
    ReferenceField
)

connect(
    host=f"mongodb://{settings.USER_MONGO}:{settings.PASSW}@{settings.MONGO_HOST}:{settings.PORT}/{settings.DB}",
    authentication_source="admin"
)


class Urls(Document):
    url = StringField(required=True, unique=True)
    domain = StringField()
    is_extract = BooleanField(default=False)
    index_at = DateTimeField(default=datetime.utcnow())

class Quotes(Document):
    text = StringField()
    author = StringField()
    tags = ListField()
    url = ReferenceField(Urls)
    extract_at = DateTimeField(default=datetime.utcnow())
