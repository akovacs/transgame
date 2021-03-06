#!/usr/bin/python
# -*- coding: utf-8 -*-

from transgame_common import *
from filelock import FileLock
from urllib import quote
import base64

gameid = param('gameid')
text = param('text')
userid = param('userid')

text = base64.b64decode(text, '-_')

text = unquote_u(text)

open('gamedata/' + gameid + '.suggestions', 'a+')

with FileLock('gamedata/' + gameid + '.suggestions') as lock:
  f = open('gamedata/' + gameid + '.suggestions', 'r+')
  output = []
  for x in f.readlines()[:-1]:
    x = x.strip()
    ctext,dummyvar,cuser = x.rpartition('|')
    if cuser == userid:
      continue
    output.append(x)
  output.append(text + '|' + userid)
  output.append('END')
  f.seek(0)
  f.write('\n'.join(output))
  f.truncate()
  f.close()

