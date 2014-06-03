import urllib2


class HttpRequest(object):

    @staticmethod
    def get_url_content(url):
        try:
            page = urllib2.urlopen(url)
            return page.read()
        except Exception:
            return ""
