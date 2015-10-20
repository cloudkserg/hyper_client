import sys
import src.hyper_mailbox
import src.hyper_api
import time
from src.hyper_api import HyperApi
from src.hipchat_api import HipchatApi
from src.comment_store import CommentStore
from src.hyper_mailbox import HyperMailbox

from conf.param import *



comment_store = CommentStore(DATABASE_FILE)

mailbox = HyperMailbox(USER, PASSWORD, SERVER)
mailbox.connect()
hyper_comments =  mailbox.get_fresh_comments(comment_store)
mailbox.close()

for hyper_comment in hyper_comments:
    hyper_comment.load_data(HyperApi(WIDGET_ID, KEY))
    comment_store.save_comment(hyper_comment)


for hyper_comment in hyper_comments:
    HipChatApi.send_message(
            HIPCHAT_URL, 
            "На странице\n" +
                hyper_comment.page.title + "\n" +
                hyper_comment.page.link + "\n" +
                "оставлен комментарий от " + hyper_comment.nick + "с текстом:\n" +
                hyper_comment.text  + "\n" +
                time.strftime('%d %b %Y, %H:%M', hyper_comment.time) + "\n" +
                hyper_comment.link
    )

print('Выслано уведомление об {0} комментариях'.format(len(hyper_comments)))







