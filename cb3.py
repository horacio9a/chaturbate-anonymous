# Chaturbate FFMPEG/STREAMLINK/LIVESTREAM/YTDL Anonymous Freechat Recorder v.2.0.0 by horacio9a for Python 3.9.1
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
from urllib3 import PoolManager
from urllib.parse import quote
from urllib.parse import unquote
from colorama import init, Fore, Back, Style
from termcolor import colored
import configparser
Config = configparser.ConfigParser()
Config.read('config3.ini')

init()
print()
print(colored(' => START <=', 'white', 'on_blue'))
print()

while True:
   try:
      mode = int(input(colored(' => Select => CB_Online_All(2) CB_Online_Wanted(1) CB_Wanted(0) => ', 'white', 'on_blue')))
      print()
      break
   except ValueError:
      print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
if mode > 2:
   print(colored(' => Too big number <=', 'white', 'on_red'))
   sys.exit()
if mode == 0:
   mod = 'CBW'
if mode == 1:
   mod = 'CBOW'
if mode == 2:
   mod = 'CBOA'

if mod == 'CBW':
  while True:
     try:
        modellist = open(Config.get('files', 'wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print(' =>',(num+1),value[:-1])
        print()
        mn = int(input(colored(' => Select CB Wanted Model => ', 'white', 'on_blue')))
        print()
        nr_lines = sum(1 for line in open(Config.get('files', 'wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print()
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected CB Wanted Model => {} <=', 'white', 'on_blue')).format(model))
  print()

if mod == 'CBOW':
  while True:
     try:
        modellist = open(Config.get('files', 'online_wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print(' =>',(num+1),value[:-1])
        print()
        mn = int(input(colored(' => Select CB Online Wanted Model => ', 'white', 'on_blue')))
        print()
        nr_lines = sum(1 for line in open(Config.get('files', 'online_wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print()
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'online_wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected CB Online Wanted Model => {} <=', 'white', 'on_blue')).format(model))
  print()

if mod == 'CBOA':
  while True:
     try:
        cboa = int(input(colored(' => Select => <500(0) <1000(1) <1500(2) <2000(3) <2500(4) <3000(5) <3500(6) => ', 'white', 'on_blue')))
        print()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  if cboa > 6:
     sys.exit()
  if cboa == 0:
     oa = 'OA500'
  if cboa == 1:
     oa = 'OA1000'
  if cboa == 2:
     oa = 'OA1500'
  if cboa == 3:
     oa = 'OA2000'
  if cboa == 4:
     oa = 'OA2500'
  if cboa == 5:
     oa = 'OA3000'
  if cboa == 6:
     oa = 'OA3500'

  if oa == 'OA500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (500, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1000, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1500, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA2000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2000, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA2500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2500, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA3000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3000, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA3500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3500, 5000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select CB Online All Models => ', 'white', 'on_blue')))
          print()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

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
 
 if 'u0022offline\\u0022' not in dec:
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
      while True:
         try:
            print()
            mode = int(input(colored(' => Mode => Exit(6) - URL(5) - YTDL(4) - LS(3) - SL(2) - FFMPEG(1) - PLAYER(0) => ', 'white', 'on_green')))
            break
         except ValueError:
            print()
            print(colored(' => Input must be a number <=', 'white', 'on_red'))
      if mode > 6:
         print()
         print(colored(' => Too big number <=', 'white', 'on_red'))
         mod = 'EXIT'
      if mode == 0:
         mod = 'PLAYER'
      if mode == 1:
         mod = 'FFMPEG'
      if mode == 2:
         mod = 'SL'
      if mode == 3:
         mod = 'LS'
      if mode == 4:
         mod = 'YTDL'
      if mode == 5:
         mod = 'URL'
      if mode == 6:
         mod = 'EXIT'

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = Config.get('folders', 'output_folder')
      fn = model + '_CB_' + timestamp
      fn1 = model + '_CB_' + timestamp + '.flv'
      fn2 = model + '_CB_' + timestamp + '.mp4'
      fn3 = model + '_CB_' + timestamp + '.ts'
      fn4 = model + '_CB_' + timestamp + '.txt'
      pf1 = (path + fn1)
      pf2 = (path + fn2)
      pf3 = (path + fn3)
      pf4 = (path + fn4)
      player = Config.get('files', 'player')
      ffmpeg = Config.get('files', 'ffmpeg')
      youtube = Config.get('files', 'youtube')
      streamlink = Config.get('files', 'streamlink')
      livestreamer = Config.get('files', 'livestreamer')

      if mod == 'PLAYER':
         print()
         print ((colored(' => PLAYER => {} <=', 'white', 'on_magenta')).format(fn))
         print()
         command = ('{} -p {} {} best'.format(streamlink, player, hlsurl))
         os.system(command)
         while True:
            try:
               print()
               prog = int(input(colored(' => Mode => URL(5) - YTDL(4) - LS(3) - SL(2) - FFMPEG(1) - Exit(0) => ', 'white', 'on_green')))
               break
            except ValueError:
               print()
               print(colored(' => Input must be a number <=', 'white', 'on_red'))
         if prog > 5:
            print()
            print(colored(' => Too big number <=', 'white', 'on_red'))
            mod = 'EXIT'
         if prog == 0:
            mod = 'EXIT'
         if prog == 1:
            mod = 'FFMPEG'
         if prog == 2:
            mod = 'SL'
         if prog == 3:
            mod = 'LS'
         if prog == 4:
            mod = 'YTDL'
         if prog == 5:
            mod = 'URL'

      if mod == 'FFMPEG':
         print()
         print ((colored(' => FFMPEG-REC => {} <=', 'white', 'on_red')).format(fn1))
         command = '{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 128k {}'.format(ffmpeg,hlsurl,pf1)
         os.system(command)
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      if mod == 'SL':
         print()
         print ((colored(' => SL-REC => {}  (  Size  @   Speed   ) <=', 'white', 'on_red')).format(fn2))
         print()
         command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf2))
         os.system(command)
         print()
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      if mod == 'LS':
         print()
         print ((colored(' => LS-REC => {}  (  Size  @   Speed   ) <=', 'white', 'on_red')).format(fn2))
         print()
         command = ('{} hlsvariant://{} best -Q -o {}'.format(livestreamer,hlsurl,pf2))
         os.system(command)
         print()
         print(colored(' => END <= ', 'white','on_blue'))
         sys.exit()

      if mod == 'YTDL':
         print()
         print ((colored(' => YTDL-REC => {}.ts <=', 'white', 'on_red')).format(fn))
         print()
         command = ('{} -i --geo-bypass --hls-use-mpegts --no-part -q --no-warnings --no-check-certificate {} -o {}'.format(youtube,hlsurl,pf3))
         os.system(command)
         print()
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      if mod == 'URL':
         print()
         print((colored(' => URL => {} <=', 'white', 'on_green')).format(fn4))
         file=open(pf4,'w')
         file.write(hlsurl)
         file.close()
         print()
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      if mod == 'EXIT':
         print()
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      else:
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
