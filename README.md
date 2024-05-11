# scrapy-mongo-example
This project is the example of how to use Scrapy with Mongodb database.

To set-up MongoDB, you can follow their instruction on the [MongoDB manual](https://www.mongodb.com/docs/manual/installation/).

## Create the `.env` File

After having the complete set of mongoDB installation and configuration, you need to create a `.env` file to store the credential URI connection string to the MongoDB engine. This file must be at the root of the spider project with the `scrapy.cfg` file.

    HOST=<hostname>
    PORT=<port_number>
    USERMONGO=<database_user>
    PASSW=<password>
    DB=<database_name>


## Custom on the `settings.py` file

In the `settings.py` of the scraper project, we need to enable the code to config with the mongoDB as below:

    import os
    from dotenv import load_dotenv
    load_dotenv()

    ITEM_PIPELINES = {
        "test_scrapy.pipelines.TestScrapyPipeline": 300,
    }

    # Adding Mong URI and DB constant
    MONGO_HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    USER_MONGO = os.getenv("USERMONGO")
    PASSW = os.getenv("PASSW")
    DB = os.getenv("DB")

## Creating `Model.py`
This idea is inspire by the Object Relational Mapping `ORM` framework from the web backend development. This `model` allow us to set the schema for storing the data accurately into the database.

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


## Custom the `pipeline.py` file
To allow the scrapy save data to `MongoDB` database, we need to have a litte bit custom on the `pipeline.py` file of the scrapy.

    from itemadapter import ItemAdapter
    from test_scrapy import settings
    from test_scrapy import model


    class TestScrapyPipeline:

        def process_item(self, item, spider):
            if spider.name != "url_index":
                data = model.Quotes(**item)

                update_url = model.Urls.objects.get(url=item.get("url", ""))
                if update_url and not update_url.is_extract:
                    update_url.is_extract = True
                    update_url.save()
            else:
                data = model.Urls(**item)
    
            data.save()
            return item

After configuring all of them above we can run crawling with or withou saving to another custom file, all data will be saved into the Mongo Dabase as expected.
