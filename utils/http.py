import urllib2
import urllib


class HttpRequest(object):

    @staticmethod
    def urlencode(url):
        return urllib.urlencode(url)

    @staticmethod
    def quote(url):
        return urllib.quote(url)

    @staticmethod
    def get_url_content(url):
        try:
            headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req)
            html = response.read()
            return html
        except Exception, e:
            return "error"