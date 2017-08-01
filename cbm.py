# Chaturbate Anonymous Freechat Mixed Recorder v.1.0.2 by horacio9a for Python 2.7.13

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
         mn = int(raw_input(" => Select CB Model URL => "))
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
print (" => Selected CB Model => %s" %model)
print

url ='https://chaturbate.com/{}/'.format(model)
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()
if "HTTP 404" not in dec:
 pwd0 = dec.split('password: ')[1]
 pwd = pwd0.split("'")[0]
 if len(pwd) < 3:
   hlsurl0 = dec.split("source src='")[1]
   hlsurl1 = hlsurl0.split("'")[0]
   if len(hlsurl1) > 1:
      hlsurl2 = hlsurl1.split('&amp')[0]
      hlsurl = re.sub('_fast_', '_', hlsurl2)
      print((colored(" => HLS URL ", 'yellow', 'on_blue')) + " => " + hlsurl + " <= ")
      print
      edge0 = dec.split('//edge')[1]
      edge = edge0.split('.')[0]
      fv0 = dec.split('CBV_2p')[1]
      fv = fv0.split('.')[0]
      rp0 = dec.split('rp=')[1]
      rp = rp0.split('&')[0]
      bg0 = dec.split("gender: '")[1]
      bg = bg0.split("'")[0]
      origin = random.randint(3,15)
      swf = 'https://chaturbate.com/static/flash/CBV_2p{}.swf'.format(fv)
      print (' => INFO => MODEL: {} * BG: {} * EDGE: {} * ORIGIN: {} <= '.format(model,bg,edge,origin))
      print

      while True:
           try:
               mode = int(raw_input(" => Select mode (1) REC or (0) PLAY => "))
               print
               break
           except ValueError:
               print
               print(colored(" => Input must be a number <= ", 'yellow', 'on_red'))
               print
      if mode == 0:
              mod = 'PLAY'
      if mode == 1:
              mod = 'REC'
      else:
              mod = 'PLAY'
      print (" => Selected Mode => (%s) <= " %mod)
      print

      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.flv'
      pf = (path + filename)
      if mod == 'PLAY':
         command = ('start ffplay -i {} -infbuf -autoexit -window_title "{} * {}"'.format(hlsurl,filename,mn))
         os.system(command)
         print((colored(" => Start PLAY ", 'yellow', 'on_red')) + " => " + filename + " <= ")
      if mod == 'REC':
         command = ('start ffplay -i {} -infbuf -autoexit -window_title "{} * {}"'.format(hlsurl,pf,mn))
         os.system(command)
         command = 'start rtmpdump -r"rtmp://edge{}.stream.highwebmedia.com/live-edge" -a"live-edge" -W"{}" -p"{}" -CS:AnonymousUser -CS:{} -CS:2.{} -CS:anonymous -CS:{} --live -y"mp4:rtmp://origin{}.stream.highwebmedia.com/live-origin/{}" -o"{}"'.format(edge,swf,url,model,fv,rp,origin,model,pf)
         os.system(command)
         print((colored(" => Start PLAY + RECORD ", 'yellow', 'on_red')) + " => " + filename + " <= ")
         print
         time.sleep(1)    # pause 1 second
         print(colored(" => END <= ", 'yellow','on_blue'))
      else:
         print
         time.sleep(1)    # pause 1 second
         print(colored(" => END <= ", 'yellow','on_blue'))
   else:
      print(colored(" => Model is PVT/HIDDEN or AWAY ", 'yellow','on_red'))
      print
      time.sleep(1)    # pause 1 second
      print(colored(" => END <= ", 'yellow','on_blue'))
 else:
   print(colored(" => Model is OFFLINE <= ", 'yellow','on_red'))
   print
   time.sleep(1)    # pause 1 second
   print(colored(" => END <= ", 'yellow','on_blue'))
else:
   print(colored(" => Page Not Found <= ", 'yellow','on_red'))
   print
   print(colored(" => Waiting for 3 seconds <= ", 'yellow','on_blue'))
   time.sleep(3)    # pause 3 second
   sys.exit()
