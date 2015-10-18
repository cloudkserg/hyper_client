# hyper_client
hyper_client

# install
pip install -r requirements.txt

# param.py
Для запуска -  пример param.py, который надо создать в корне
SERVER = 'pop.gmail.com'
USER = 'hoper@gmail.com'
PASSWORD = 'selenium'

WIDGET_ID = 27798
KEY = '32323423'

HIPCHAT_URL = 'https://api.hipchat.com/v2/room/23423423'

# description param.py

SERVER - адрес почты
USER - пользователь почты
PASSWORD - пароль к почте

WIDGET_ID - ид виджет hyper comment
KEY - ключ для hyper comment

HIPCHAT_URL - юрл для группы hipchat, куда слать комментарии (полученный https://www.hipchat.com/docs/apiv2)

# run
Запускать - envname/bin/python3 main.py

# description
Берет новую почту с адреса - USER,
ищет почту о hyper comments
вытаскивает по ним данные через api
и шлет новые сообщения 
на https://vestnik.hipchat.com/chat/room/1952241


# change

Формат сообщения можно поправить в main.py
