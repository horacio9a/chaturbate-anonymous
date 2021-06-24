# Chaturbate FFMPEG Remote Anonymous Freechat Recorder v.2.0.0 by horacio9a for Python 2.7.18
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read('config.ini')

init()
print
print(colored(' => START <=', 'white', 'on_blue'))
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
  print(colored(' => Wrong model name or banned <=', 'white','on_red'))
  print
  print(colored(' => END <=', 'white','on_blue'))
  sys.exit()

 if 'u0022offline\\u0022' not in dec:
   status0 = dec.split('status\\u0022: ')[1]
   status1 = status0.split(', \\u0022room')[0]
   status = status1.replace('\\u0022', '')
   print ((colored(' => Status => {} <=', 'white', 'on_green')).format(status))
   print

   if 'public' in status:
      hlsurl0 = dec.split('https://edge')[1]
      hlsurl1 = hlsurl0.split('m3u8')[0]
      hlsurl2 = hlsurl1.replace('\\u002D', '-')
      hlsurl = ('https://edge{}m3u8'.format(hlsurl2))
      print ((' => HlsUrl => {} <=').format(hlsurl))
      print

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

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Age: ({}) * Gender: ({}) <=', 'white', 'on_blue')).format(rn,loc,age,bg))

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = Config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.flv'
      pf = (path + filename)
      ffmpeg = Config.get('files', 'ffmpeg')
	  
      print
      print (colored(' => FFMPEG-REC => {} <=', 'white', 'on_red')).format(filename)
      command = ('{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 128k {}'.format(ffmpeg,hlsurl,pf))
      os.system(command)
      print
      print(colored(' => END <=', 'white','on_blue'))
      sys.exit()

   else:
      print ((colored(' => Model is {} <=', 'white', 'on_red')).format(status))
      print
      print(colored(' => END <=', 'white','on_blue'))
      sys.exit()

 else:
   print(colored(' => Model is offline <=', 'white','on_red'))
   print
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()

else:
   print(colored(' => Page Not Found <=', 'white','on_red'))
   print
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()