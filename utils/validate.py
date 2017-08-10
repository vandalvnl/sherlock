class UrlLink():

    @staticmethod
    def containsWWW(url):
        if 'www.' in url:
            return True
        return False

    @staticmethod
    def contains_http(url):
        if 'http://' in url:
            return url
        elif 'https://' in url:
            return url.replace('https://', 'http://')
        return False

    @staticmethod
    def makeDomain(url, complement):
        if UrlLink.containsWWW:
            return "http://" + complement.replace("\n", "") + "." + url
        else:
            url = url.replace("www.", "")
            return "http://" + complement.replace("\n", "") + "." + url
