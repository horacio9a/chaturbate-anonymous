# Chaturbate STREAMLINK Remote Anonymous Freechat Recorder v.1.1.1 by horacio9a for Python 2.7.16
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, random, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

init()
print
print(colored(' => START <=', 'yellow', 'on_blue'))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]


url ='https://chaturbate.com/{}/'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = (r.data)
dec=urllib.unquote(enc)

if 'HTTP 404' not in dec:
 try:
  pwd0 = dec.split('broadcaster_username')[1]
  pwd = pwd0.split(':')[0]
 except:
  print(colored(' => Wrong model name or banned <=', 'yellow','on_red'))
  print
  print(colored(' => END <=', 'yellow','on_blue'))
  sys.exit()

 if 'u0022offline' not in dec:
  hlsurl0 = dec.split('u0022https:')[1]
  hlsurl1 = hlsurl0.split('\u0022,')[0]

  if len(hlsurl1) > 180:
   print(colored(' => Try again <=', 'yellow','on_blue'))
   sys.exit()
  else:
   pass

   if len(hlsurl1) > 50:
      hlsurl2 = re.sub('//', 'https://', hlsurl1)

      server1 = hlsurl2.split('\u002Dhls')[0]
      server = re.sub('live', 'live-hls/', server1)

      try:
         rp = hlsurl2.split('sd\u002D')[1]
      except:
         rp = hlsurl2.split('ws\u002D')[1]

      hlsurl = ('{}amlst:{}-sd-{}'.format(server,model,rp))

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

      bg0 = dec.split('gender\u0022: \u0022')[1]
      bg = bg0.split('\u0022')[0]

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Age: ({}) * Gender: ({}) <=', 'yellow', 'on_blue')).format(rn,loc,age,bg))

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.mp4'
      pf = (path + filename)
      streamlink = config.get('files', 'streamlink')

      print
      print (colored(' => SL-REC >>> {} <<<', 'yellow', 'on_red')).format(filename)
      print
      command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf))
      os.system(command)
      print
      print(colored(' => END <= ', 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(' => Model is PVT/HIDDEN or AWAY <=', 'yellow','on_red'))
      print
      print(colored(' => END <=', 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(' => Model is OFFLINE <=', 'yellow','on_red'))
   print
   print(colored(' => END <=', 'yellow','on_blue'))
   sys.exit()

else:
   print(colored(' => Page Not Found <=', 'yellow','on_red'))
   print
   print(colored(' => END <=', 'yellow','on_blue'))
   sys.exit()
