import hashlib
import json
import requests

class HyperApi():
    COMMENT_URL = 'http://c1api.hypercomments.com/1.0/comments/get'
    COMMENT_LIST_URL =  'http://c1api.hypercomments.com/1.0/comments/list'
    widget_id = None
    key = None

    def __init__(self, widget_id, key):
        self.widget_id = widget_id
        self.key = key

    def _create_sign(self, body):
        string = body + self.key
        return hashlib.sha1(string.encode('utf-8')).hexdigest()

    def post_request(self, url, params = {}):
        params['widget_id'] = self.widget_id
        params_string = json.dumps(params)
        sign = self._create_sign(params_string)
        payload = {'body': params_string, 'signature': sign}

        r = requests.post(url, data=payload).json()

        if r['result'] != 'success':
            raise Exception("Not right response from page(%s) with data(%s): %s" % (url, params_string, str(r)))

        if len(r['data']) == 0:
            return {}

        return r['data'][0]


    def get_comment_data(self, link, comment_id, xid):
        return self.post_request(self.COMMENT_URL, {'link': link, 'id': comment_id, 'xid': xid})

    def get_comments_data(self, link):
        return self.post_request(self.COMMENT_LIST_URL, {'link': link, 'sort': 'new', 'limit': 1, 'offset': 0})
