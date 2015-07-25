#!/usr/bin/python
# -*- coding:gbk -*-
#   lgy
#2015-07-11
import mysql.connector
import sys
import random
import string
import hashlib


def ProductIp():
      ip = '%s'%(random.randint(1,254))
      ip += '.'
      ip += '%s'%(random.randint(1,254))
      ip += '.'
      ip += '%s'%(random.randint(1,254))
      ip += '.'
      ip += '%s'%(random.randint(1,254))
      return ip

def JudgeYear(year):
      if year % 400 == 0:
            return True
      elif year % 4 == 0 & year % 100 != 0:
            return True
      else:
            return False
      
def ProductData():
      year = random.randint(2013,2015)
      month = random.randint(1,12)
      day = ''
      if month == 2:
            if JudgeYear(year):
                  day = '%02d'%(random.randint(1,29))
            else:
                  day = '%02d'%(random.randint(1,28))
      elif month == 1 | month == 3 | month == 5 | month == 7 | month == 8 |month == 10 |month == 12:
            day = '%02d'%(random.randint(1,31))
      else:
            day = '%02d'%(random.randint(1,30))
      Data = '%d'%year
      Data += '-'
      Data += '%02d'%month
      Data += '-'
      Data += day
      return Data

def ProductTime():
      hour = '%02d'%(random.randint(0,23))
      minite = '%02d'%(random.randint(0,59))
      sec = '%02d'%(random.randint(0,59))
      return hour+':'+minite+':'+sec

def ProductUrl(ProductType,Ip):
      Url = 'http://'
      if ProductType:
            if Ip == '':
                  Ip = ProductIp()
            Url += Ip+':'
            Url += random.choice(['8080/','53/','23/','8000/'])
      else:
            Url += 'www.'
            lengthD = random.randint(5,10)
            Url += string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',lengthD)).replace(' ','')
            Url += random.choice(['.com/','.org/','.edu.cn/','.edu/','.com.cn/'])
      num = random.randint(2,6)
      for i in range(0,num):
            length = random.randint(5,10)
            Url += string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',length)).replace(' ','')
            Url += '/'
      Url += string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',length)).replace(' ','')
      return Url

def ProductVirusName():
      Virus = 'a.'
      length = random.randint(5,10)
      Virus += string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',length)).replace(' ','')
      Virus += '.'
      length = random.randint(5,10)
      Virus += string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',length)).replace(' ','')
      Virus += random.choice(['.c','.a','.d'])
      return Virus

def ProductIDodData(Type,IDnumber):
      ID = ''
      if Type == 1:
            ID = 'MM-2015-'
      elif Type == 2:
            ID = 'MU-2015-'
      elif Type == 3:
            ID = 'MM-S-2015-'
      else :
            ID = 'MI-2015-'
      if Type != 2:
            ID += '%07d'%IDnumber
      else:
            ID += '%010d'%IDnumber
      return ID

def ProductAppName():
      return random.choice(['taobao','baidu','360','jingdong','360Freewifi','Dajie','Fetion','iReader','JDIM','kuxun','letv','QQBrowser',\
                            'qqmusic','QQReader','RenRen','sina','sogou','sohu','UC','wandoujia','youku','yuntuv','zhibo8','zzenglish'])

def ProductAppMD5(AppName):
##      length = random.randint(5,10)
##      App = string.join(random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',length)).replace(' ','')
      m = hashlib.md5()
      m.update(AppName)
      AppMD5 = m.hexdigest()
      return AppMD5

##def ProductAction():
      # coding=gbk
##      return random.choice(['恶意扣费','恶意流量','恶意短信','读写文件'])
def ProductAction():
      ##return random.choice(['信息窃取','远程控制','恶意扣费','恶意传播','信息窃取','资源消耗','流氓行为'])
      return random.choice(['information stealing', 'malware propagation', 'remote control', 'resource degradation', 'roguery','Malicious deduction'])

def ProductOperationSystem():
      return random.choice(['IOS','Android'])

def ProductAppStoreName():
      # coding=gbk
##      return random.choice(['新浪','百度','360','安智网','腾讯应用宝','155安卓','91助手','应用汇'])
      return random.choice(['sina','baidu','360','AnzhiWeb','Tengxunyingyongbao','155 Android','91 helper','yingyonghui'])

def ProductPort():
      return random.randint(0,65535)
def ProductRiskLevel():
      return random.randint(1,7)    #暂时随机生成

def ProductMobileIMEI():
      IMEI = string.join(random.sample('01234567890123456789',14)).replace(' ','')
      IMEI += '0'
      return IMEI
def ProductProtocol():
      return random.choice(['TCP/IP', 'NetBEUI', 'IPX/SPX','UDP','HTTP','FTP'])

##print ProductProtocol()
##print ProductMobileIMEI()
##print ProductAppStoreName()
##print ProductAction()
##print ProductAppMD5()
##print ProductIDodData(1,19087)
##print ProductIDodData(2,17678)
##print ProductIDodData(3,15345)
##print ProductVirusName()
##print ProductUrl(1,'192.168.2.123')
#print string.join(random.sample('zyxwvutsrqponmlkjihgfedcba',5)).replace(' ','')

      
      
