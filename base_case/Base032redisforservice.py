__author__ = 'kirry'

import unittest
import time,sys
from interfaceTest.Methods.BeopTools import BeopTools
import redis


class Base032(unittest.TestCase):
    testCaseID = 'Base032'
    projectName = ''
    buzName = "监控Redis服务器的连接数"
    info = {
        "rnbtech.redis.cache.chinacloudapi.cn":("Ny/HnFe7nBUR18t+aeatzbOEQJMX1skGB//Rns2aw6o=",6379),
        "usredis.redis.cache.windows.net":("X+0rTyQymbjT7G26/mQzXj3PZvrUkYB73oagFnHnFfs=",6379),
        "beopdemo.rnbtech.com.hk":("beopweb:rnbtechrd",6379)
            }






    def setUp(self):
        self.error = []
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
        for info in self.info:
            rv = self.getInfo(host=info,passwd=self.info[info][0],port=self.info[info][1])
            connected_clients = rv.get("connected_clients")
            if connected_clients>5000:
                self.error. append("链接redis地址为%s中的连接数大于5000，当前为%s"%(info,connected_clients))
            else:
                print("链接redis地址为%s中的连接数正常！当前为%s"%(info,connected_clients))
        a = BeopTools()
        a.raiseError(self.error,self.testCaseID)



    def getInfo(self,host,port,passwd):
        conn = False
        try:
            pool = redis.ConnectionPool(host=host,port=port,password=passwd,max_connections=1)
            conn = redis.StrictRedis(connection_pool=pool,db=0)
        except Exception as e:
            assert False,"链接redis时出现错误，错误信息为%s"%e.__str__()
        if conn:
            return conn.info()




if __name__ == "__main__":
    way = 1
    while way:
        suite = unittest.TestSuite()
        suite.addTest(Base032('Test'))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        time.sleep(60)