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
    is_extract = BooleanField(default=False)
    index_at = DateTimeField(default=datetime.utcnow())

class Quotes(Document):
    text = StringField()
    author = StringField()
    tags = ListField()
    url = ReferenceField(Urls)
    extract_at = DateTimeField(default=datetime.utcnow())
