import urllib2


class HttpRequest(object):

    @staticmethod
    def get_url_content(url):
        try:
            headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req)
            html = response.read()
            return html
        except Exception:
            return "hello world"
