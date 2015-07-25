import mysql.connector
import sys
import random
import string
def ProductData():
    Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
    MyCursor = Mysql.cursor()
    #生成IP地址字符串
    for num in range(0,1000):
        ip = '%s'%(random.randint(1,254))
        ip += '.'
        ip += '%s'%(random.randint(1,254))
        ip += '.'
        ip += '%s'%(random.randint(1,254))
        ip += '.'
        ip += '%s'%(random.randint(1,254))
        port = random.randint(1000,32768)
        RiskLevel = random.randint(1,7)
        malevolenceType = random.choice(['information stealing', 'malware propagation', 'remote control', 'resource degradation', 'roguery','Malicious deduction'])
        number = 'MM-2015-0000'
        number += string.join(random.sample(['1','2','3','4','5','6','7','8','9'], 4)).replace(" ","")
        sql = 'insert into ipblacklist values(%s ,%s ,%s ,%d ,%d)'%(number,ip,malevolenceType,port,RiskLevel)
        MyCursor.execute('insert into ipblacklist values("%s" ,"%s" ,"%s" ,%d ,%d)'%(number,ip,malevolenceType,port,RiskLevel))
        Mysql.commit()
    MyCursor.close()
    Mysql.close()
    print 'insert success'
def UpdateAllRiskLevel():
    Mysql = mysql.connector.connect(user = 'root',password = 'liguoyu123',database = 'test',use_unicode = True)
    MyCursor = Mysql.cursor()
    #更新urlbalcklist中的RiskLevel值
    IsEmpty = MyCursor.execute('select * from urlblacklist')
    if IsEmpty == None:
        dataList = MyCursor.fetchall()
        for data in dataList:
            MyCursor.execute('update urlblacklist set RiskLevel = %d where number = "%s"'%(random.randint(1,7),data[0]))
            Mysql.commit()
    #更新malevolenceapp 中的RiskLevel值
    IsEmpty = MyCursor.execute('select * from malevolenceapp')
    if IsEmpty == None:
        dataList = MyCursor.fetchall()
        for data in dataList:
            MyCursor.execute('update malevolenceapp set RiskLevel = %d where number = "%s"'%(random.randint(1,7),data[0]))
            Mysql.commit()
    #更新ipblacklist 中的RiskLevel值
    IsEmpty = MyCursor.execute('select * from ipblacklist')
    if IsEmpty == None:
        dataList = MyCursor.fetchall()
        for data in dataList:
            MyCursor.execute('update ipblacklist set RiskLevel = %d where number = "%s"'%(random.randint(1,7),data[0]))
            Mysql.commit()
    MyCursor.close()
    Mysql.close()
    print 'insert success'

#执行函数
UpdateAllRiskLevel()
