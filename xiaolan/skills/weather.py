# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import logging
import json
import pygame
import requests
import urllib2
import re
import socket
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import speaker
from recorder import recorder

def start():

    main()

def main():

    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    r = recorder()
    location = 'zhongshan'
    host = 'https://api.seniverse.com/v3/weather/now.json?key='
    key = 'sxyi6ehxblxkqeto'
    APIURL = key + '&location=' + location + '&language=zh-Hans&unit=c'
    
    url = host + APIURL

    r = requests.get(url)
    
    json = r.json()
    weather = json['now']['text']
    temperature = json['now']['temperature']
    humidity = json['now']['humidity']
    
    tweatherstates = ',今天,' + weather + '，温度是,'  + temperature + '，摄氏度，'
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
