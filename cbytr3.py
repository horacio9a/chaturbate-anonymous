# Chaturbate YOUTUBE-DL Remote Anonymous Freechat Recorder v.1.0.9 by horacio9a for Python 3.8.0
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

if 'HTTP 404' not in dec:
 try:
  pwd0 = dec.split('broadcaster_username')[1]
  pwd = pwd0.split(':')[0]
 except:
  print(colored(' => Wrong model name or banned <=', 'yellow','on_red'))
  print()
  print(colored(' => END <=', 'yellow','on_blue'))
  sys.exit()

 if 'u0022offline' not in dec:
  hlsurl0 = dec.split('u0022https:')[1]
  hlsurl1 = hlsurl0.split(',')[0]

  if len(hlsurl1) > 180:
   print(colored(' => Try again <=', 'yellow','on_blue'))
   sys.exit()
  else:
   pass

   if len(hlsurl1) > 50:
      hlsurl2 = re.sub('//', 'https://', hlsurl1)
      hlsurl3 = re.sub('u002Dsd', '', hlsurl2)
      hlsurl3 = re.sub('u002Dws', '', hlsurl2)

      server = hlsurl2.split('live')[0]

      rp1 = hlsurl3.split('amlst:')[1]
      rp2 = rp1.split('\\u002D')[1]
      rp = rp2.split('_trns')[0]

      hlsurl = ('{}live-hls/amlst:{}-sd-{}_trns_h264/playlist.m3u8'.format(server,model,rp))

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

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Age: ({}) * Sex: ({}) <=', 'yellow', 'on_blue')).format(rn,loc,age,bg))

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
