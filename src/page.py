import requests
import re

class Page():
    scheme = None
    link = None
    xid = None
    title = None

    def __init__(self, link, scheme):
        self.scheme = scheme
        self.link = link
        self.define_xid()

    def define_xid(self):
        page_html = requests.get(self.link).text

        m = re.search('xid: \'(.*)\'', page_html)
        if m is None or len(m.group(1)) == 0:
            raise Exception('Page %s not compare xid' % self.link)

        self.xid = m.group(1)
