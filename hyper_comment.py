class HyperComment():
    comment_id = None
    page = None

    parent_comment = None
    nick = None
    text = None
    time = None

    def __init__(self, comment_id, page):
        self.comment_id = comment_id
        self.page = page


    def load_data(self, api):
        data = api.get_comment_data(self.page.link, self.comment_id, self.page.xid)
        if len(data) == 0:
            raise Exception('Not find data for comment {0} page {1} '.format(self.comment_id, self.page.xid))
        
        self.page.title = data['page_title']

        self.text = data['text']
        self.time = data['time']
        self.nick = data['nick']

        if data['parent_id'] is not None:
            parent_comment = HyperComment(data['parent_id'], self.page)
            parent_comment.text = data['text']
            parent_comment.time = data['time']
            parent_comment.nick = data['nick']

            self.parent_comment = parent_comment
