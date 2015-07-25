#-*- codeing:utf-8 -*-
#   lgy
#2015-07-11

import ProductData
import mysql.connector
import random
import threading

def ProductIpBlackListData():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      for i in range(0,100000):
            Ip = ProductData.ProductIp()
            Action = ProductData.ProductAction()
##            print Action
            number = ProductData.ProductIDodData(4,i+1)
            Risklev = ProductData.ProductRiskLevel()
            Port = ProductData.ProductPort()
            sql = 'insert into ipblacklist values(%s ,%s ,%s ,%d ,%d)'%(number,Ip,Action,Port,Risklev)
            MyCursor.execute('insert into ipblacklist values("%s" ,"%s" ,"%s" ,%d ,%d)'%(number,Ip,Action,Port,Risklev))
            ##'insert into ipblacklist values("%s" ,"%s" ,"%s" ,%d ,%d)'%(number,Ip,Action,Port,Risklev)
            Mysql.commit()
            if i %100 == 0:
                  print 'Ip 进度：%4.2f%%'%(float(i/100))
      MyCursor.close()
      Mysql.close()
def ProductUrlBlackListData():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      for i in range(0,100000):
            Url = ProductData.ProductUrl(random.randint(0,1),'')
            number = ProductData.ProductIDodData(2,i+1)
            Risklev = ProductData.ProductRiskLevel()
            datatime = ProductData.ProductData()
            datatime += ' '
            datatime += ProductData.ProductTime()
            MyCursor.execute('insert into urlblacklist values("%s" ,"%s","%s",%d)'%(number,Url,datatime,Risklev))
            Mysql.commit()
            if i %100 == 0:
                  print 'Url 进度：%4.2f%%'%(float(i/100))
      MyCursor.close()
      Mysql.close()
def ProductAppBlackListData():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      for i in range(0,100000):
            AppMD5 = ProductData.ProductAppMD5()
            number = ProductData.ProductIDodData(1,i+1)
            Risklev = ProductData.ProductRiskLevel()
            datatime = ProductData.ProductData()
            Action = ProductData.ProductAction()
            Sys = ProductData.ProductOperationSystem()
            MyCursor.execute('insert into appblacklist values("%s" ,"%s","%s","%s" ,"%s",%d)'%(number,AppMD5,Action,Sys,datatime,Risklev))
            Mysql.commit()
            if i %100 == 0:
                  print 'App 进度：%4.2f%%'%(float(i/100))
      MyCursor.close()
      Mysql.close()
def ProductVirusListData():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      for i in range(0,100000):
            Url = ProductData.ProductUrl(random.randint(0,1),'')
            Virus = ProductData.ProductVirusName()
            number = ProductData.ProductIDodData(3,i+1)
            Risklev = ProductData.ProductRiskLevel()
            datatime = ProductData.ProductData()
            Store = ProductData.ProductAppStoreName()
            Sys = ProductData.ProductOperationSystem()
            MyCursor.execute('insert into Virus values("%s" ,"%s","%s","%s" ,"%s",%d)'%(number,Store,Virus,Url,datatime,Risklev))
            Mysql.commit()
            if i %100 == 0:
                  print 'Virus 进度：%4.2f%%'%(float(i/100))
      MyCursor.close()
      Mysql.close()

def ProductAction():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      MyCursor.execute('create table if not exists Active(SouIp varchar(18),SouPort int,DesIp varchar(18),DesPort int,Protocol varchar(16),Virus varchar(64),\
                        Store varchar(32),Sys varchar(32),DataTime varchar(20),IMEI varchar(16),Url varchar(256),ProcessName varchar(32),MD5 varchar(256))')
      Mysql.commit()
      MyCursor.execute('delete from Active')
      Mysql.commit()
      for i in range(0,100000):
            SouIp = ProductData.ProductIp()
            DesIp = ProductData.ProductIp()
            SouPort = ProductData.ProductPort()
            DesPort = ProductData.ProductPort()
            Url = ProductData.ProductUrl(0,'')
            Virus = ProductData.ProductVirusName()
            DataTime = ProductData.ProductData()+' '+ProductData.ProductTime()
            Store = ProductData.ProductAppStoreName()    
            Sys = ProductData.ProductOperationSystem()
            Protocol = ProductData.ProductProtocol()
            IMEI = ProductData.ProductMobileIMEI()
            ProcessName = ProductData.ProductAppName()
            MD5 = ProductData.ProductAppMD5(ProcessName)
            MyCursor.execute('insert into Active values("%s",%d,"%s",%d,"%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(SouIp,SouPort,DesIp,DesPort,Protocol,Virus,Store,Sys,DataTime,IMEI,Url,ProcessName,MD5))
            Mysql.commit()
            if i %100 == 0:
                  print 'Active 进度：%4.2f%%'%(float(i/100))
            
      MyCursor.close()
      Mysql.close()

      
def TableOperation():
      Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
      MyCursor = Mysql.cursor()
      
      MyCursor.execute('create table if not exists Virus(number varchar(18),ShopName varchar(32),Virus varchar(32),Address varchar(256),Data_Time varchar(10),RiskLevel int)')
      MyCursor.execute('create table if not exists urlblacklist(number varchar(32),URL varchar(255),DataTime varchar(25),RiskLevel int)')
      MyCursor.execute('create table if not exists ipblacklist(number varchar(32),ip varchar(16),MalevolenceType varchar(32),port int,RiskLevel int)')
      MyCursor.execute('create table if not exists appblacklist(number varchar(255),md5 varchar(255),malevolenceType varchar(32),OS varchar(32),datatime varchar(32),RiskLevel int)')
      MyCursor.execute('delete from Virus')
      MyCursor.execute('delete from urlblacklist')
      MyCursor.execute('delete from ipblacklist')
      MyCursor.execute('delete from appblacklist')
      Mysql.commit()
      MyCursor.close()
      Mysql.close()


      
def main():
      choice = int(raw_input('造黑名单数据(1)/行为数据：(2)'))
      if choice == 1:
            TableOperation()
            t1 = threading.Thread(target=ProductIpBlackListData)
            t2 = threading.Thread(target=ProductUrlBlackListData)
            t3 = threading.Thread(target=ProductAppBlackListData)
            t4 = threading.Thread(target=ProductVirusListData)
            print '线程1----'
            t1.start()
            print '线程2----'
            t2.start()
            print '线程3----'
            t3.start()
            print '线程4----'
            t4.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            print 'finished!'
      else:
            ProductAction()
if __name__ == '__main__':
      main()




