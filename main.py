import sys
import hyper_mailbox
import hyper_api
from hipchat_api import HipChat


from param import *


mailbox = hyper_mailbox.HyperMailbox(USER, PASSWORD, SERVER)
mailbox.connect()
hyper_comments =  mailbox.get_comments()
mailbox.close()

for hyper_comment in hyper_comments:
    hyper_comment.load_data(hyper_api.HyperApi(WIDGET_ID, KEY))


for hyper_comment in hyper_comments:
    HipChat.send_message(HIPCHAT_URL, 'На странице ' + hyper_comment.page.title + ' оставлен комментарий от ' + hyper_comment.nick + ' с текстом ' + hyper_comment.text)

print('Выслано уведомление об {0} комментариях'.format(len(hyper_comments)))







