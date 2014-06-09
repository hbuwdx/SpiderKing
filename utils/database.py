import pymongo


class MongodbClient(object):

    def __init__(self, database, host='localhost', port=27017):
        self.__client = pymongo.Connection(host, port)
        self.__database = self.__client[database]
        self.__collections = {}

    def get_client(self):
        return self.__client

    def get_database(self):
        return self.__database

    def collection(self, collection_name):
        if collection_name in self.__collections:
            return self.__collections.get(collection_name)
        else:
            collection = self.get_database()[collection_name]
            self.__collections[collection_name] = collection
            return collection


def clean():
    client = MongodbClient("spider")
    client.collection("count").remove()
    print client.collection("urls").remove()
    print client.collection("todo_urls").remove()


def status():
    client = MongodbClient("spider")
    print client.collection("urls").count()
    print client.collection("todo_urls").count()
    print client.collection("count").find({"name": "todo_urls"})[0]["count"]
    print client.collection("count").update({"name": "urls"},  {"$set": {"count": 0}})
    print client.collection("count").update({"name": "todo_urls"},  {"$set": {"count": 1}})

# status()
clean()