__author__ = 'kirry'
import socket
import unittest
import time
import datetime, sys, json,ssl
from interfaceTest import app
from interfaceTest.Methods.BeopTools import BeopTools
import pymongo
from bson.son import SON
from pymongo import MongoClient

class Base031(unittest.TestCase):
    testCaseID = 'Base031'
    projectName = ''
    buzName = "增加对天气数据的监控"
    mongoIp = '101.37.90.188'
    mogoPoint = 27018
    usename = "beopweb"
    passwd = "RNB.beop-2013"





    def setUp(self):
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.startTimeStamp = time.time()
        self.logger = BeopTools.init_log(r'%s\log\%s.txt' % (sys.path[0], self.testCaseID))
        self.a = BeopTools()
    def tearDown(self):
        CaseUseTime = time.time() - self.startTimeStamp
        CaseUseTime = str('%.2f秒' % CaseUseTime)
        print("本次用例执行时间为%s" % CaseUseTime)
        self.endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def Test(self):
        error = []
        now = datetime.datetime.now()
        if now.minute in [30,31,32,33,34,35]:
            recordHours = (now - datetime.timedelta(hours = 8))
            deltimes = recordHours.replace(minute=0,second=0,hour=0,microsecond=0)
            redata = ["US4151921","CN101020600"]
            for i in redata:
                commd = {"utc_time":deltimes}
                data = self.connectMogoData(self.mongoIp,self.mogoPoint,i,commd)
                datalength = data[0]["value"].get(str(recordHours.hour)).get("0")
                if len(datalength)== 0:
                    error.append("mongo数据库中的表%s,天气更新数据为空！可能导致天气数据没有更新！"%i)
                else:
                    print("数据正常！")

            a = BeopTools()
            a.raiseError(error,self.testCaseID)
        else:
            print("没到运行时间！")


    def connectMogoData(self,host,point,table,commd):
        con = False
        data = []
        try:
            con = MongoClient(host=host,port=point)
            db = con.weatherdata
            db.authenticate(self.usename,self.passwd)
            #dt = db.command('aggregate', 'DataSourceAdditional', pipeline=self.commd, explain=True)
            dt = db[table].find(commd)
            for i in dt:
                data.append(i)
        except Exception as e:
            assert 0,e
        finally:
            if con:
                con.close()
        return data



if __name__ == "__main__":
    while True:
        suite = unittest.TestSuite()
        suite.addTest(Base031('Test'))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        time.sleep(60)