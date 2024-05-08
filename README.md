# scrapy-mongo-example
This project is the example of how to use Scrapy with Mongodb database.

To set-up MongoDB, you can follow their instruction on the [MongoDB manual](https://www.mongodb.com/docs/manual/installation/).

## Create the `.env` File

After having the complete set of mongoDB installation and configuration, you need to create a `.env` file to store the credential URI connection string to the MongoDB engine. This file must be at the root of the spider project with the `scrapy.cfg` file.

    MONGO_URI=mongodb://{username}:{password}@localhost:27017/
    MONGO_DB={database_name}


## Custom on the `settings.py` file

In the `settings.py` of the scraper project, we need to enable the code to config with the mongoDB as below:

    import os
    from dotenv import load_dotenv
    load_dotenv()

    ITEM_PIPELINES = {
        "test_scrapy.pipelines.TestScrapyPipeline": 300,
    }

    # Adding Mong URI and DB constant
    MONGO_URI = os.getenv("MONGO_URI") or "mongodb://localhost:27017/"
    MONGO_DB = os.getenv("MONGO_DB") or "defautl_db"

## Custom the `pipeline.py` file
To allow the scrapy save data to `MongoDB` database, we need to have a litte bit custom on the `pipeline.py` file of the scrapy.

    import pymongo
    from itemadapter import ItemAdapter
    from test_scrapy import settings


    class TestScrapyPipeline:
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB]

        def process_item(self, item, spider):
            self.db[spider.name].insert_one(dict(item))

            return item

After configuring all of them above we can run crawling with or withou saving to another custom file, all data will be saved into the Mongo Dabase as expected.
