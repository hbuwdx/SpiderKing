import re
import gl
from utils.http import HttpRequest
from utils.file import File
from utils.date import *


class Spider(object):

    @staticmethod
    def get_url_tuple(url):
        http_or_https = "http://"
        domain = ""
        relative_url = ""
        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            http_or_https = "https://"
            url = url.replace("https://", "")
        else:
            url
        index = url.find("/")
        if index != -1:
            domain = url[0:index]
            relative_url = url[index:]
        return (http_or_https,domain,relative_url)

    @staticmethod
    def fetch(url, thread):
        http_or_https, domain, relative_url = Spider.get_url_tuple(url)
        new_url_id = gl.db.collection(gl.DB_COUNT).find_one({"name": gl.DB_URLS_NAME})["count"]+1
        new_document_path = gl.DOCUMENT_ROOT_PATH+domain+"\\"
        new_document_name = new_url_id.__str__()+".html"
        url_dict = {
            "id": new_url_id,
            "url": HttpRequest.quote(url),
            "http_or_https": http_or_https,
            "domain": domain,
            "relative_url": relative_url,
            "document_path": new_document_path,
            "document_name": new_document_name,
            "create_time": get_time_million(),
        }
        gl.db.collection(gl.DB_URLS_NAME).insert(url_dict)
        gl.db.collection(gl.DB_COUNT).update({"name": gl.DB_URLS_NAME}, {"$inc": {"count": 1}})
        page = HttpRequest.get_url_content(url)
        File.makedir(new_document_path)
        File.write_text_to_file(new_document_path+new_document_name, page)
        new_urls = Spider.get_page_hrefs(page)
        for i in range(len(new_urls)):
            new_url = {
                "id": gl.db.collection(gl.DB_COUNT).find_one({"name": gl.DB_TODO_URLS_NAME})["count"]+1,
                "url": new_urls[i],
            }
            if gl.db.collection(gl.DB_TODO_URLS_NAME).find({url: new_urls[i]}).count() <= 0:
                gl.db.collection(gl.DB_TODO_URLS_NAME).insert(new_url)
                gl.db.collection(gl.DB_COUNT).update({"name": gl.DB_TODO_URLS_NAME}, {"$inc": {"count": 1}})
        thread.task = None
        thread.working = False

    @staticmethod
    def get_page_hrefs(page):
        p = re.compile(r'href=[\"\'](.*?)[\"\']', re.IGNORECASE)
        m = p.findall(page)
        return m

    @staticmethod
    def get_page_title(page):
        p = re.compile(r'<title>(.*)</title>', re.IGNORECASE)
        m = p.findall(page)
        return m[0].decode(Spider.get_page_charset(page))

    @staticmethod
    def get_page_charset(page):
        p = re.compile(r'charset=(.*)[\"\']', re.IGNORECASE)
        m = p.findall(page)
        return m[0]