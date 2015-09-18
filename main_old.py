import requests
import hashlib
import sys
import json

from param import *

def create_sign(body):
    string = body + KEY
    return hashlib.sha1(string.encode('utf-8')).hexdigest()

def post_request(url, params = {}):
    params['widget_id'] = WIDGET_ID

    params_string = json.dumps(params)

    sign = create_sign(params_string)

    payload = {'body': params_string, 'signature': sign}

    return requests.post(url, data=payload).json()

def get_data(r):
    if r['result'] != 'success' or len(r['data']) == 0:
        raise Exception('Not right response from page:' + str(r))

    return r['data'][0]



def get_page_data(url):
    r = post_request(API_PAGE_URL, {'link': url})

    return get_data(r)

def get_count_new_comments(url, old_data):
    data = get_page_data(url)
    
    diff_removed = data['cm_removed'] - old_data['cm_removed']
    diff_comments = data['cm2'] - old_data['cm2']

    diff = diff_comments + diff_removed

    return (diff if diff > 0 else 0)

    
old_data = {'cm2': 0, 'cm_removed': 0}
count = get_count_new_comments(MAIN_LINK, old_data)

if count > 0:
    print(str(count) + ' новых комментариев на странице')
else:
    print('Новых комментариев нету')


