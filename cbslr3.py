# Chaturbate STREAMLINK Remote Anonymous Freechat Recorder v.1.1.2 by horacio9a for Python 3.9.1
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
print(colored(' => START <=', 'white', 'on_blue'))
print()

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://chaturbate.com/{}/'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = quote(r.data)
dec= unquote(enc)

if 'HTTP 404' not in dec:
 try:
  pwd0 = dec.split('broadcaster_username')[1]
  pwd = pwd0.split(':')[0]
 except:
  print(colored(' => Wrong model name or banned <=', 'white','on_red'))
  print()
  print(colored(' => END <=', 'white','on_blue'))
  sys.exit()

 if 'u0022offline' not in dec:
   status0 = dec.split('status\\u0022: ')[1]
   status1 = status0.split(', \\u0022room')[0]
   status = status1.replace('\\u0022', '')
   print ((colored(' => Status => {} <=', 'white', 'on_green')).format(status))
   print ()

   if 'public' in status:
      hlsurl0 = dec.split('https://edge')[1]
      hlsurl1 = hlsurl0.split('m3u8')[0]
      hlsurl2 = hlsurl1.replace('\\u002D', '-')
      hlsurl = ('https://edge{}m3u8'.format(hlsurl2))
      print ((' => HlsUrl => {} <=').format(hlsurl))
      print ()

      try:
         rn0 = dec.split('Real Name:</div>\n                            <div class="data">')[1]
         rn = rn0.split('</div>')[0]
      except:
         rn = '-'

      try:
         loc0 = dec.split('Location:</div>\n                            <div class="data">')[1]
         loc = loc0.split('</div>')[0]
      except:
         loc = '-'

      try:
         age0 = dec.split('Age:</div>\n                                <div class="data">')[1]
         age = age0.split('</div>')[0]
      except:
         age = '-'

      try:
         bg0 = dec.split('Sex:</div>\n                            <div class="data">')[1]
         bg = bg0.split('</div>')[0]
      except:
         bg = '-'

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Age: ({}) * Sex: ({}) <=', 'white', 'on_blue')).format(rn,loc,age,bg))

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.mp4'
      pf = (path + filename)
      streamlink = config.get('files', 'streamlink')

      print()
      print((colored(' => SL-REC >>> {} <<<', 'white', 'on_red')).format(filename))
      print()
      command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf))
      os.system(command)
      print()
      print(colored(' => END <=', 'white','on_blue'))
      sys.exit()

   else:
      print ((colored(' => Model is {} <=', 'white', 'on_red')).format(status))
      print()
      print(colored(' => END <=', 'white','on_blue'))
      sys.exit()

 else:
   print(colored(' => Model is offline <=', 'white','on_red'))
   print()
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()

else:
   print(colored(' => Page Not Found <=', 'white','on_red'))
   print()
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()
