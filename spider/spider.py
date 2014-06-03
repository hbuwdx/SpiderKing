import re

from utils.http import HttpRequest
from utils.file import File
from utils.date import *
from logic.queue import *


class Spider(object):

    manager = None

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
        File.append_text_to_file("E:\\spiderData\\urls.txt", url)
        http_or_https, domain, relative_url = Spider.get_url_tuple(url)
        page = HttpRequest.get_url_content(url)
        File.makedir("E:\\spiderData\\"+domain)
        File.write_text_to_file("E:\\spiderData\\"+domain+"\\"+get_time_million().__str__()+".html", page)
        new_urls = Spider.get_page_hrefs(page)
        for i in range(len(new_urls)):
            File.append_text_to_file("E:\\spiderData\\temp.txt", new_urls[i])
            Spider.manager.task_queue.append(Task(1, new_urls[i], 1))
        thread.task = None
        thread.working = False
        return new_urls

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