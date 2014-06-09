from logic.download import *
from utils.database import *
from logic.queue import *


DB_NAME = "spider"
DB_URLS_NAME = "urls"
DB_DOCUMENT_NAME = "document"
DOCUMENT_ROOT_PATH = "E:\\spiderData\\"
DB_TODO_URLS_NAME = "todo_urls"
DB_COUNT = "count"

task_queue = TaskQueue()
thread_pool = ThreadPool(50, 60)
db = MongodbClient(DB_NAME)
db.collection(DB_COUNT).insert({"name": DB_URLS_NAME, "count": 0})
db.collection(DB_COUNT).insert({"name": DB_TODO_URLS_NAME, "count": 1})
db.collection(DB_TODO_URLS_NAME).insert({"id":1,"url":"http://ifeng.com/"})