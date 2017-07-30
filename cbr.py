# Chaturbate Remote Anonymous Freechat RTMP Recorder v.1.0.1 by horacio9a for Python 2.7.13

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
pnf0 = dec.split('canc')[1]
pnf = pnf0.split('d')[0]
if len(pnf) > 5:
 pwd0 = dec.split('password: ')[1]
 pwd = pwd0.split(',')[0]
 if len(pwd) > 3:
   hlsurl0 = dec.split("source src='")[1]
   hlsurl1 = hlsurl0.split("'")[0]
   if len(hlsurl1) > 1:
      rp0 = hlsurl1.split('rp=')[1]
      rp = rp0.split('&')[0]
      print((colored(" => RP ", 'yellow', 'on_blue')) + " => " + rp + " <= ")
      print
      edge0 = dec.split('//edge')[1]
      edge = edge0.split('.')[0]
      fv0 = dec.split('CBV_2p')[1]
      fv = fv0.split('.')[0]
      bg0 = dec.split("gender: '")[1]
      bg = bg0.split("'")[0]
      origin = random.randint(3,15)
      swf = 'https://chaturbate.com/static/flash/CBV_2p{}.swf'.format(fv)
      print (' => INFO => MODEL: {} * BG: {} * EDGE: {} * ORIGIN: {} <=\n'.format(model,bg,edge,origin))
      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp + '.flv'
      pf = (path + filename)
      print((colored(" => Start RECORD ",'yellow','on_red')) + " => " + filename + " <=\n")
      command = 'rtmpdump -r"rtmp://edge{}.stream.highwebmedia.com/live-edge" -a"live-edge" -W"{}" -p"{}" -CS:AnonymousUser -CS:{} -CS:2.{} -CS:anonymous -CS:{} --live -y"mp4:rtmp://origin{}.stream.highwebmedia.com/live-origin/{}" -o"{}"'.format(edge,swf,url,model,fv,rp,origin,model,pf)
      os.system(command)
      print(colored("\n => END <= ", 'yellow','on_blue'))
      time.sleep(3)    # pause 3 second
      sys.exit()
   else:
      print(colored(" => Model is PVT/HIDDEN or AWAY\n", 'yellow','on_red'))
      print(colored(" => Waiting for 60 seconds <= ", 'yellow','on_blue'))
      time.sleep(60)    # pause 60 second
      print(colored(" => END <= ", 'yellow','on_blue'))
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
