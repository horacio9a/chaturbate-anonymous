# Chaturbate FFPLAY/FFMPEG Anonymous Freechat Recorder v.1.0.3 by horacio9a for Python 2.7.13

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
print
print(colored(" => START <= ", 'yellow', 'on_blue'))
print

while True:
     try:
         modellist = open(config.get('files', 'model_list'),'r')
         for (num,value) in enumerate(modellist):
            print ' =>',(num+1),value[:-1]
         print
         mn = int(raw_input(colored(" => Select CB Model URL => ", 'yellow', 'on_blue')))
         print
         break
     except ValueError:
         print
         print(colored(" => Input must be a number <= ", 'yellow', 'on_red'))
         print
model_url = open(config.get('files', 'model_list'), 'r').readlines()[mn-1][:-1]
model0 = model_url.split('://')[1]
model1 = model0.split('/')[1]
model = re.sub('/', '', model1)
print (colored(' => Selected CB Model => {} <=', 'yellow', 'on_blue')).format(model)
print

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

      while True:
           try:
               print
               mode = int(raw_input(colored(" => Select mode (1) REC or (0) PLAY => ", 'yellow', 'on_blue')))
               break
           except ValueError:
               print(colored("\n => Input must be a number <= ", 'yellow', 'on_red'))
      if mode == 0:
              mod = 'PLAY'
      if mode == 1:
              mod = 'REC'
      else:
              mod = 'PLAY'
      print
      print (colored(' => Selected Mode => {} <=', 'yellow', 'on_blue')).format(mod)

      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.flv'
      pf = (path + filename)

      if mod == 'PLAY':
         print
         print (colored(' => Start ffplay PLAY => {} <=', 'white', 'on_magenta')).format(filename)
         command = ('ffplay -hide_banner -loglevel panic -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {}"'.format(hlsurl,filename,mn))
         os.system(command)

      if mod == 'REC':
         print
         print (colored(' => Start ffmpeg RECORD => {} <=', 'white', 'on_red')).format(filename)
         command = ('ffmpeg -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 160k -f flv {}'.format(hlsurl,pf))
         os.system(command)
         time.sleep(1)    # pause 1 second
         print(colored(" => END <= ", 'yellow','on_blue'))
         sys.exit()

      else:
         print
         time.sleep(1)    # pause 1 second
         print(colored(" => END <= ", 'yellow','on_blue'))
         sys.exit()

   else:
      print(colored(" => Model is PVT/HIDDEN or AWAY ", 'yellow','on_red'))
      print
      time.sleep(1)    # pause 1 second
      print(colored(" => END <= ", 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(" => Model is OFFLINE <= ", 'yellow','on_red'))
   print
   time.sleep(1)    # pause 1 second
   print(colored(" => END <= ", 'yellow','on_blue'))
   sys.exit()

else:
   print(colored(" => Page Not Found <= ", 'yellow','on_red'))
   print
   print(colored(" => Waiting for 3 seconds <= ", 'yellow','on_blue'))
   time.sleep(3)    # pause 3 second
   sys.exit()
