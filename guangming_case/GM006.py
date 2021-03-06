﻿__author__ = 'sophia'
import time
import datetime
import unittest

from interfaceTest.Methods.BeopTools import *
from interfaceTest import app


class GM006(unittest.TestCase):
    testCaseID = 'GM006'
    projectName = "光明项目"
    buzName = 'get_history_data_padded接口返回是否有数据'
    start = 0.0
    now = 0
    startTime = ""
    errors = []

    def setUp(self):
        self.start = datetime.datetime.now()
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.logger = BeopTools.init_log(r'%s\log\%s.txt' % (sys.path[0], self.testCaseID))

    def Test(self):
        self.errors = []
        self.check()
        if self.errors:
            BeopTools.writeLogError(self.logger, '\n'.join(self.errors))
            BeopTools.raiseError(self.errors, self.testCaseID)
        else:
            BeopTools.writeLogError(self.logger, '错误个数为0!')



    def check(self):
        addr = "http://%s/get_history_data_padded" % (app.config['SERVERIP'])
        timeEnd = self.start.strftime("%Y-%m-%d 23:00:00")
        timeStart = self.start.strftime("%Y-%m-%d 00:00:00")
        data={"projectId":425,"pointList":["20010000000044_T","20010000000044_H","20010000000044_A","20010000000044_S"],
              "timeStart":timeStart,"timeEnd":timeEnd,"timeFormat":"m5"}
        rt=None
        rt = BeopTools().postToken(url=addr, Data=data,timeout=20,name=app.config['NAME'],passwd=app.config['PWD'],loginUrl="http://%s/login"%app.config['SERVERIP'])
        if rt and isinstance(rt, dict) and rt.get("error",False):
            self.errors.append("错误信息光明移动点9L1226,9L1227,9L1228历史轨迹回放接口预期有值实际返回值为%s" % (str(rt)))
        else:
            print("返回的结果有值")

    def tearDown(self):
        self.offline = False
        use1 = str((datetime.datetime.now() - self.start).seconds)
        use = use1 + "s"
        print("本次用例执行时间为%s" % use)
        self.now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GM006('Test'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

