__author__ = 'kirry'
import socket
import unittest
import time
import datetime, sys, json,ssl
from interfaceTest import app
from interfaceTest.Methods.BeopTools import BeopTools
from pymongo import MongoClient
import pymysql
from pymysql.cursors import Cursor
status = Cursor
status._defer_warnings = True

class Base029(unittest.TestCase):
    testCaseID = 'Base029'
    projectName = ''
    buzName = "对光明乳业实时数据的监控添加旧库检测"
    sqlIp = "118.178.93.236"
    sqlname = "root"
    sqlPasswd = "RNBtech1103"
    sqlPoint = 3306
    sqldata = "bdtm"
    sqllist = {
        "数据未及时更新":'''select a.group, h.*, rt.data, rt.alarm as late from (
    select r.identifying, max(r.time) as latest from bdtm.historydata as r
    group by r.identifying
) as h
inner join bdtm.active_data as a on h.identifying = a.identifying
inner join bdtm.realtimedata as rt on rt.identifying = a.identifying
where a.active = 1 and (data = 0.0 or alarm = 1) and datediff(now(), latest) > 2
order by latest,a.group'''
    }
    settime = None




    def setUp(self):
        self.error = []
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.startTimeStamp = time.time()
        self.logger = BeopTools.init_log(r'%s\log\%s.txt' % (sys.path[0], self.testCaseID))
        self.a = BeopTools()

    def Test(self):
        for sql in self.sqllist:
            data = self.connectMysql(self.sqllist[sql])[0]
            if data.__len__()>30:
                self.error.append({sql:data})
        print(self.error)
        cleardata = []
        if self.error:
            for er in self.error:
                data = []
                keys = list(er.keys())[0]
                values = er.get(keys)
                for mess in values:
                    dt = []
                    for info in mess:
                        if isinstance(info,datetime.datetime):
                            dt.append(datetime.datetime.strftime(info,"%Y-%m-%d %H:%M:%S"))
                        else:
                            dt.append(info)
                    data.append(dt)
                cleardata.append([keys,data])
            self.error = []
            for message in cleardata:
                title = message[0]+":共%s条"%len(message[1])
                body = [str(i) for i in message[1]]
                self.error.append(title+"\n"+"\n".join(body))
            self.error = ["\n".join(self.error)]

        self.a.raiseError(self.error,self.testCaseID)






    def connectMysql(self,sql):
        datas = []
        cur,conn = False,False
        try:
            conn = pymysql.Connection(user=self.sqlname, passwd=self.sqlPasswd,
                     host=self.sqlIp,port=self.sqlPoint, db=self.sqldata,charset='utf8')
            cur = conn.cursor()
            cur.execute(sql)
            datas.append(cur.fetchall())
        except Exception as e:
            assert 0,"错误信息为：%s"%e.__str__()
        finally:
            if conn:
                if cur:
                    cur.close()
                conn.close()
        return datas


    def tearDown(self):
        CaseUseTime = time.time() - self.startTimeStamp
        CaseUseTime = str('%.2f秒' % CaseUseTime)
        print("本次用例执行时间为%s" % CaseUseTime)
        self.endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Base029('Test'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)