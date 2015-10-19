import mailbox
from bs4 import BeautifulSoup
from page import Page 
import hyper_comment
import re
from urllib.parse import urlparse


class HyperMailbox(mailbox.Mailbox):

    def _get_hyper_messages(self):
        hyper_messages = []
        for message in self.get_messages():
            if 'HyperComments notification' in message.get('Subject'):
                hyper_messages.append(message)
        return hyper_messages

    def _find_comment_link(self, s):
        return s.find('a', href=re.compile('#hcm=\w+'))

    def get_comments(self):
        hyper_comments = []
        for message in self._get_hyper_messages():
            data = self.get_message_data(message)
            s = BeautifulSoup(str(data), 'html.parser')
            link = self._find_comment_link(s)
            if link is None:
                raise Exception('link not found in ' + str(data))
            
            href = link.get('href')
            o = urlparse(href)
            comment_id = o.fragment.split('=')[1]

            page = Page(o.scheme + '://' + o.netloc + o.path, o.scheme)
            comment = hyper_comment.HyperComment(comment_id, page)

            hyper_comments.append(comment)

        return hyper_comments
