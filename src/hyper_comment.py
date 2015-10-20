import time
class HyperComment():
    comment_id = None
    page = None

    parent_comment = None
    nick = None
    text = None
    time = None
    link = None

    def __init__(self, comment_id, page):
        self.comment_id = comment_id
        self.page = page
        self.link = self.page.link + '#hcm=' + self.comment_id


    def _parse_time(self, data):
        return time.localtime(int(data['unixtime']))

    def load_data(self, hyper_api):
        data = hyper_api.get_comment_data(self.page.link, self.comment_id, self.page.xid)
        if len(data) == 0:
            raise Exception('Not find data for comment {0} page {1} '.format(self.comment_id, self.page.xid))
        
        self.page.title = data['page_title']

        self.text = data['text']
        self.time = self._parse_time(data)
        self.nick = data['nick']

        if data['parent_id'] is not None:
            parent_comment = HyperComment(data['parent_id'], self.page)
            parent_comment.text = data['text']
            parent_comment.time = self._parse_time(data)
            parent_comment.nick = data['nick']

            self.parent_comment = parent_comment


