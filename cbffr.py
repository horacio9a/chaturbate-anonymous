# Chaturbate Remote FFPLAY/FFMPEG Anonymous Freechat Recorder v.1.0.3 by horacio9a for Python 2.7.13

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, random, command
urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print(colored("\n => START <= ", 'yellow', 'on_blue'))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://chaturbate.com/{}/'.format(model)
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

if "HTTP 404" not in dec:
 pwd0 = dec.split(' password: ')[1]
 pwd = pwd0.split("'")[0]

 if "currently offline" not in dec:
   hlsurl0 = dec.split("source src='")[1]
   hlsurl1 = hlsurl0.split("'")[0]

   if len(hlsurl1) > 1:
      hlsurl2 = hlsurl1.split('&amp')[0]
      hlsurl = re.sub('_fast_', '_', hlsurl2)
      print (colored(' => HLS URL => {} <=', 'yellow', 'on_blue')).format(hlsurl)
      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.flv'
      pf = (path + filename)

      print
      print (colored(' => Start ffmpeg RECORD => {} <=', 'white', 'on_red')).format(filename)
      command = ('ffmpeg -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 160k {}'.format(hlsurl,pf))
      os.system(command)
      time.sleep(1)    # pause 1 second
      print(colored(" => END <= ", 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(" => Model is PVT/HIDDEN or AWAY\n", 'yellow','on_red'))
      print(colored(" => Waiting for 60 seconds <= ", 'yellow','on_blue'))
      time.sleep(60)    # pause 60 second
      print(colored(" => END <= ", 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(" => Model is OFFLINE <=\n", 'yellow','on_red'))
   print(colored(" => Waiting for 60 seconds <= ", 'yellow','on_blue'))
   time.sleep(60)    # pause 60 second
   sys.exit()

else:
   print(colored(" => Page Not Found <= ", 'yellow','on_red'))
   print
   print(colored(" => Waiting for 60 seconds <= ", 'yellow','on_blue'))
   print
   time.sleep(60)    # pause 60 second
   sys.exit()
