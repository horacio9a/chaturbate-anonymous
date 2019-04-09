# Chaturbate FFPLAY/LIVESTREAMER/STREAMLINK/FFMPEG/YTDL Anonymous Freechat Recorder v.1.0.8 by horacio9a for Python 2.7.16
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

while True:
   try:
      mode = int(raw_input(colored(' => Select => CB_Online_All(2) CB_Online_Wanted(1) CB_Wanted(0) => ', 'yellow', 'on_blue')))
      print
      break
   except ValueError:
      print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
if mode > 2:
   print(colored(' => Too big number <=', 'yellow', 'on_red'))
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
        modellist = open(config.get('files', 'wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print ' =>',(num+1),value[:-1]
        print
        mn = int(raw_input(colored(' => Select CB Wanted Model => ', 'yellow', 'on_blue')))
        print
        nr_lines = sum(1 for line in open(config.get('files', 'wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'yellow', 'on_red'))
           print
           print(colored(' => END <=', 'yellow','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
  model = open(config.get('files', 'wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected CB Wanted Model => {} <=', 'yellow', 'on_blue')).format(model))
  print

if mod == 'CBOW':
  while True:
     try:
        modellist = open(config.get('files', 'online_wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print ' =>',(num+1),value[:-1]
        print
        mn = int(raw_input(colored(' => Select CB Online Wanted Model => ', 'yellow', 'on_blue')))
        print
        nr_lines = sum(1 for line in open(config.get('files', 'online_wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'yellow', 'on_red'))
           print
           print(colored(' => END <=', 'yellow','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
  model = open(config.get('files', 'online_wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected CB Online Wanted Model => {} <=', 'yellow', 'on_blue')).format(model))
  print

if mod == 'CBOA':
  while True:
     try:
        cboa = int(raw_input(colored(' => Select => <500(0) <1000(1) <1500(2) <2000(3) <2500(4) <3000(5) <3500(6) => ', 'yellow', 'on_blue')))
        print
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
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
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA1000':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA1500':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA2000':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA2500':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA3000':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

  if oa == 'OA3500':
    while True:
       try:
          modellist = open(config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select CB Online All Model => ', 'yellow', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'yellow', 'on_red'))
             print
             print(colored(' => END <=', 'yellow','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'yellow', 'on_red'))
    model = open(config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected CB Online All Model => {} <=', 'yellow', 'on_blue')).format(model))
    print

url ='https://chaturbate.com/{}/'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

if 'has been banned' in dec:
 print(colored(' => This room is banned <=', 'yellow','on_red'))
 print
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
  print
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
      hlsurl = hlsurl1.split('?')[0]

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

      print ((colored(' => INFO => Real Name: ({}) * Location: ({}) * Gender: ({}) <=', 'yellow', 'on_blue')).format(rn,loc,bg))
      while True:
         try:
            print
            prog = int(raw_input(colored(' => Mode => Exit(6) => URL(5) => YTDL(4) => SL(3) => LS(2) => FF-FLV(1) => FF-VIEW(0) => ', 'yellow', 'on_blue')))
            break
         except ValueError:
            print(colored('\n => Input must be a number <=', 'yellow', 'on_red'))
      if prog > 6:
         print(colored('\n => Too big number <=', 'yellow', 'on_red'))
         prg = 'EXIT'
      if prog == 0:
         prg = 'FF-VIEW'
      if prog == 1:
         prg = 'FF-FLV'
      if prog == 2:
         prg = 'LS'
      if prog == 3:
         prg = 'SL'
      if prog == 4:
         prg = 'YTDL'
      if prog == 5:
         prg = 'URL'
      if prog == 6:
         prg = 'EXIT'

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp
      fn1 = model + '_CB_' + timestamp + '.flv'
      fn2 = model + '_CB_' + timestamp + '.mp4'
      fn3 = model + '_CB_' + timestamp + '.ts'
      fn4 = model + '_CB_' + timestamp + '.txt'
      pf1 = (path + fn1)
      pf2 = (path + fn2)
      pf3 = (path + fn3)
      pf4 = (path + fn4)
      ffmpeg = config.get('files', 'ffmpeg')
      ffplay = config.get('files', 'ffplay')
      livestreamer = config.get('files', 'livestreamer')
      streamlink = config.get('files', 'streamlink')
      youtube = config.get('files', 'youtube')

      if prg == 'FF-VIEW':
         print
         print (colored(' => FF-PLAY => {} <=', 'yellow', 'on_magenta')).format(filename)
         command = ('{} -hide_banner -loglevel panic -i {} -vf scale=640:480 -infbuf -framedrop -autoexit -window_title "{} * {} {}"'.format(ffplay,hlsurl,filename,mn,mod))
         os.system(command)
         while True:
            try:
               prog = int(raw_input(colored(' => Mode => URL(5) => YTDL(4) => SL(3) => LS(2) => FF-FLV(1) => Exit(0) => ', 'yellow', 'on_blue')))
               break
            except ValueError:
               print(colored('\n => Input must be a number <=', 'yellow', 'on_red'))
         if prog > 5:
            print(colored('\n => Too big number <=', 'yellow', 'on_red'))
            prg = 'EXIT'
         if prog == 0:
            prg = 'EXIT'
         if prog == 1:
            prg = 'FF-FLV'
         if prog == 2:
            prg = 'LS'
         if prog == 3:
            prg = 'SL'
         if prog == 4:
            prg = 'YTDL'
         if prog == 5:
            prg = 'URL'
         if prog == 6:
            prg = 'EXIT'

      if prg == 'FF-FLV':
         print
         print (colored(' => FF-FLV-REC => {} <=', 'yellow', 'on_red')).format(fn1)
         command = '{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 160k {}'.format(ffmpeg,hlsurl,pf1)
         os.system(command)
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      if prg == 'LS':
         print
         print (colored(' => LS-REC >>> {}.mp4 <<<', 'yellow', 'on_red')).format(filename)
         print
         command = ('{} hlsvariant://{} best -Q -o {}'.format(livestreamer,hlsurl,pf2))
         os.system(command)
         print
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      if prg == 'SL':
         print
         print (colored(' => SL-REC >>> {}.mp4 <<<', 'yellow', 'on_red')).format(filename)
         print
         command = ('{} hls://{} best -Q -o {}'.format(streamlink,hlsurl,pf2))
         os.system(command)
         print
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      if prg == 'YTDL':
         print
         print (colored(' => YTDL-REC => {}.ts <=', 'yellow', 'on_red')).format(filename)
         print
         command = ('{} -i --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf3))
         os.system(command)
         print
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      if prg == 'URL':
         print
         print(colored(' => URL => {} <=', 'white', 'on_green')).format(fn4)
         file=open(pf4,'w')
         file.write(hlsurl)
         file.close()
         print
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      if prg == 'EXIT':
         print
         print(colored(' => END <=', 'yellow','on_blue'))
         sys.exit()

      else:
         print
         print(colored(' => END <=', 'yellow','on_blue'))
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
