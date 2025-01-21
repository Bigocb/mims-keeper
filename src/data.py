'''
Responsible for connection to the datastore and saving the given object
'''
import dataclasses
from dataclasses import dataclass
import logging

import pymongo
import datetime

from pymongo import MongoClient


@dataclass
class Interaction:
    prompt: str
    response: str
    tags: list[str] = None
    topic: str = ""
    createdon: datetime = datetime.datetime.now()


class Data:

    # Initiate connection with MonogoDB Atlas
    def get_connection(self):
        try:
            client: MongoClient = pymongo.MongoClient(
            "mongodb+srv://bobbycloutier:RUF7R33rv1KLTYMh@cluster0.1tduo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
            db: object = client.mims
            return db.interactions
        except ConnectionError as e:
            logging.error("There was an error connecting to Atlas: %s", e, exc_info=True)

    # Save interaction object to mongo atlas
    def save(self, inter: Interaction) -> int:

        # Connect to DB and insert
        col = self.get_connection()
        interaction_id = col.insert_one(dataclasses.asdict(inter))

        return interaction_id


