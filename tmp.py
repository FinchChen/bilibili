# -*- coding: UTF-8 -*-

import requests

tmp = requests.get('https://www.iyingdi.cn/feed/list/seed/v2?web=1&seed=2&system=web').json().get('feeds')[0].get('feed')

a = tmp.get('title')
print a.encode('unicode')