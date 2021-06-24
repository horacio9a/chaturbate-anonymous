# Chaturbate Anonymous Get Online Wanted Models v.2.0.0 by horacio9a for Python 2.7.18
# coding: utf-8

import sys, os, ssl, configparser
Config = configparser.ConfigParser()
Config.read('config.ini')

wanted_model_list = open(Config.get('files', 'wanted_model_list'),'r')
online_all_model_list = open(Config.get('files', 'online_all_model_list'),'r')
online_wanted_model_list = (set(online_all_model_list).intersection(wanted_model_list))
for (num,value) in enumerate(online_wanted_model_list):
	print value[:-1]
	if len(online_wanted_model_list) < 1:
	    print(online_wanted_model_list)
