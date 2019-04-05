# Chaturbate YOUTUBE-DL Remote Anonymous Freechat Recorder v.1.0.8 by horacio9a for Python 3.8.0
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, random, command
urllib3.disable_warnings()
from urllib3 import PoolManager
from urllib.parse import quote
from urllib.parse import unquote
from colorama import init, Fore, Back, Style
from termcolor import colored
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

init()
print()
print(colored(' => START <=', 'yellow', 'on_blue'))
print()

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://chaturbate.com/{}/'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = quote(r.data)
dec= unquote(enc)

if 'has been banned' in dec:
 print(colored(' => This room is banned <=', 'yellow','on_red'))
 print()
 print(colored(' => END <=', 'yellow','on_blue'))
 sys.exit()

else:
 pass

if 'HTTP 404' not in dec:
 try:
  pwd0 = dec.split(' password: ')[1]
  pwd = pwd0.split("'")[0]
 except:
  print(colored(' => Wrong model name <=', 'yellow','on_red'))
  print()
  print(colored(' => END <=', 'yellow','on_blue'))
  sys.exit()

 if 'currently offline' not in dec:
  hlsurl0 = dec.split("source src='")[1]
  hlsurl1 = hlsurl0.split("'")[0]

  if len(hlsurl1) > 180:
   print(colored(' => Try again <=', 'yellow','on_blue'))
   sys.exit()
  else:
   pass

   if len(hlsurl1) > 1:
      hlsurl2 = hlsurl1.split('?')[0]
      hlsurl = re.sub('_fast_', '_', hlsurl2)

      try:
         rn0 = dec.split('Real Name:</dt><dd>')[1]
         rn = rn0.split('</dd>')[0]
      except:
         rn = '-'

      try:
         loc0 = dec.split('Location:</dt><dd>')[1]
         loc = loc0.split('</dd>')[0]
      except:
         loc = '-'

      bg0 = dec.split("gender: '")[1]
      bg = bg0.split("'")[0]

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Gender: ({}) <= ', 'yellow', 'on_blue')).format(rn,loc,bg))

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.ts'
      pf = (path + filename)
      youtube = config.get('files', 'youtube')

      print()
      print((colored(' => YTDL-REC => {} <=', 'yellow', 'on_red')).format(filename))
      print()
      command = ('{} -i --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf))
      os.system(command)
      print()
      print(colored(' => END <=', 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(' => Model is PVT/HIDDEN or AWAY <=', 'yellow','on_red'))
      print()
      print(colored(' => END <=', 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(' => Model is OFFLINE <=', 'yellow','on_red'))
   print()
   print(colored(' => END <=', 'yellow','on_blue'))
   sys.exit()

else:
   print(colored(' => Page Not Found <=', 'yellow','on_red'))
   print()
   print(colored(' => END <=', 'yellow','on_blue'))
   sys.exit()
