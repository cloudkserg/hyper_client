# hyper_client
hyper_client

# install
pip install -r requirements.txt

# Запуск
# Делаем из базы conf/comment_store.sqlite.dest файл conf/comment_store.sqlite
# Делаем из conf/param.py.dest файл conf/param.py

#example param.py
USER = 'hoper@gmail.com'
PASSWORD = 'selenium'

WIDGET_ID = 27798
KEY = '32323423'

HIPCHAT_URL = 'https://api.hipchat.com/v2/room/23423423'
DATABASE_FILE = 'comment_store.sqlite'

# description param.py

SERVER - адрес почты
USER - пользователь почты
PASSWORD - пароль к почте

WIDGET_ID - ид виджет hyper comment
KEY - ключ для hyper comment

HIPCHAT_URL - юрл для группы hipchat, куда слать комментарии (полученный https://www.hipchat.com/docs/apiv2)
DATABASE_FILE - файл с базой данных sqlite3


# run
Запускать - python3 main.py

# description
Берет новую почту с адреса - USER,
ищет почту о hyper comments
вытаскивает по ним данные через api
и шлет новые сообщения 
на https://vestnik.hipchat.com/chat/room/1952241


# change

Формат сообщения можно поправить в main.py
