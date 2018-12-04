import datetime
import time
import json
from collections import namedtuple

now = datetime.datetime.now()
time.sleep(1)
tenmin = now - datetime.timedelta(minutes=10)
print now
print tenmin

s = '{"a": "hehe"}'

print s

j = json.loads(s)
json_obj = json.loads(
    s, object_hook=lambda d: namedtuple('x', d.keys())(*d.values()))

print j
print json_obj