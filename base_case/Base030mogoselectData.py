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

class Base030(unittest.TestCase):
    testCaseID = 'Base030'
    projectName = ''
    buzName = "对同一个原始点绑定多个云点的行为进行监控"
    mongoIp = '101.37.90.188'
    mogoPoint = 27020
    usename = "beopweb"
    passwd = "RNB.beop-2013"
    commd = [
{
  '$match': {
    'type': 4,
    'params.mapping.point': {'$exists': 1}
  }
},
{
  '$group':{
    '_id': {
      'projId': '$projId',
      'rtname': '$params.mapping.point'
    },
    'count': SON({'$sum': 1})
  }
},
{
  '$match': {
    'count': SON({'$gte': 2})
  }
}
]




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
        data = self.connectMogoData(self.mongoIp,self.mogoPoint)

    def connectMogoData(self,host,point):
        con = False
        data = []
        try:
            con = MongoClient(host=host,port=point)
            db = con.beopdata
            db.authenticate(self.usename,self.passwd)
            #dt = db.command('aggregate', 'DataSourceAdditional', pipeline=self.commd, explain=True)
            dt = db.DataSourceAdditional.aggregate(self.commd, allowDiskUse = True)
            for i in dt:
                data.append(i)
        except Exception as e:
            assert 0,e
        finally:
            if con:
                con.close()
        return data



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Base030('Test'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)