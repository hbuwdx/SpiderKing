import re

from utils.http import HttpRequest
from utils.file import File
from utils.date import *
from logic.queue import *


class Spider(object):

    manager = None

    @staticmethod
    def get_url_host(url):
        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            url = url.replace("https://", "")
        else:
            url
        index = url.find("/")
        if index != -1:
            url = url[1:index]
        return url

    @staticmethod
    def fetch(url):
        host = Spider.get_url_host(url)
        page = HttpRequest.get_url_content(url)
        File.append_text_to_file("E:\\spiderData\\urls.txt", url)
        File.makedir("E:\\spiderData\\"+host)
        File.write_text_to_file("E:\\spiderData\\"+host+"\\"+get_time_million()+".html", page)
        new_urls = Spider.get_page_hrefs(page)
        for i in range(len(new_urls)):
            Spider.manager.task_queue.append(Task(1, new_urls[i], 1))
        return new_urls

    @staticmethod
    def get_page_hrefs(page):
        p = re.compile(r'href=[\"\'](.*?)[\"\']', re.IGNORECASE)
        m = p.findall(page)
        return m