import time
import random
import string
import hashlib
import hmac
import re
from urllib.parse import unquote
import base64
import requests


def get_hawk_header(id, key, uri, method):
    ts = int(time.time())
    nonce = generate_random_string(6)
    mac = calculate_mac(ts, nonce, key, uri, method)
    obj = f'Hawk id="{id}", ts="{ts}", nonce="{nonce}", mac="{mac}"'
    return obj


def generate_random_string(size):
    random_source = string.ascii_letters + string.digits  # 包含大小写字母和数字
    len_source = len(random_source)
    result = []
    for _ in range(size):
        result.append(random_source[random.randint(0, len_source - 1)])
    return ''.join(result)


def calculate_mac(ts, nonce, key, uri, method):
    uri_json = parse_uri(uri)
    host = uri_json['host'].lower()
    port = uri_json['port']
    resource = uri_json['resource']
    context = f'hawk.1.header\n{ts}\n{nonce}\n{method.upper()}\n{resource}\n{host}\n{port}\n\n\n'.encode('utf-8')
    # print("context=", context)
    mac_str = hmac.new(key.encode('utf-8'), context, hashlib.sha256).digest()
    mac = base64.b64encode(mac_str).decode('utf-8')
    return mac


def parse_uri(input_uri):
    uri_regex = re.compile(r'^([^:]+)\:\/\/(?:[^@/]*@)?([^\/:]+)(?:\:(\d+))?([^#]*)(?:#.*)?$')
    parts = uri_regex.match(input_uri)
    if not parts:
        return {'host': '', 'port': '', 'resource': ''}

    scheme = parts.group(1).lower()
    uri_json = {
        'host': parts.group(2),
        'port': parts.group(3) or (scheme == 'http' and '80' or (scheme == 'https' and '443' or '')),
        'resource': unquote(parts.group(4))
    }
    return uri_json


if __name__ == '__main__':
    id = '7643597634433345'
    key = 'b53c5b43be524e69a5b338fb1074e52a'
    uri = 'https://api.huodongxing.com/v3/Manage/CreateActivity'
    method = 'POST'

    hawk_header = get_hawk_header(id, key, uri, method)
    # hawk_header = 'Hawk id="4583604759278164", ts="1696844776", nonce="whd0mF", mac="6eZdOdT0CEg8XpYuz9yhApSw+N097lwof8FpMhuVqV0="'
    header = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": hawk_header}
    # print(header)
    res = requests.post(url='https://api.huodongxing.com/v3/Manage/CreateActivity',
                        headers=header,
                        data={"category": 0, "tag": 0})
    if res.ok:
        print(res.text)
