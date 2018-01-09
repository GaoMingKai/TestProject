__author__ = 'kirry'
import datetime,time
from interfaceTest import app
from interfaceTest.Methods.BeopTools import BeopTools
import unittest,json


class Calc046(unittest.TestCase):
    testCaseID = 'Calc046'
    projectName = ""
    buzName = '凯德项目中重要虚拟点更新时间的监控'
    startTime = ""
    datas = {
        "539":{"Day_data_Summary":25,"Day_data_Summary1":25,"Day_data_Summary2":25,"Day_data_Summary3":25,"Day_data_Summary4":25,"Plant_Load_forecast":4},
        "542":{"Day_data_Summary":25,"Day_data_Summary1":25},
        "540":{"Day_data_Summary":25,"Day_data_Summary1":25,"Day_data_Summary2":25,"Plant_Load_forecast":4},
        "528":{"Day_data_Summary":25,"Plant_Load_forecast":4}
    }
    url = "http://%s/get_realtimedata_time"%app.config["SERVERIP"]



    def setUp(self):
        self.errors = []
        self.start = datetime.datetime.now()

    def Test(self):
        now = datetime.datetime.now()
        if now.hour in [12]:
            errorData = {}
            for dt in self.datas:
                errorpoint = []
                projectData = self.datas[dt]
                rv = self.getdata(dt,list(projectData.keys()))
                if rv and isinstance(rv,dict):
                    for pointName in projectData:
                        roundTime = projectData[pointName]
                        gettime = rv.get(pointName)
                        pointTime = datetime.datetime.strptime(gettime,"%Y-%m-%d %H:%M:%S")
                        delTime = (now - pointTime).total_seconds()/3600 if now>pointTime else (pointTime - now).total_seconds()/3600
                        if delTime>roundTime:
                            errorpoint.append(pointName)
                        else:
                            print("项目id为%s的项目中虚拟点数据正常为%s"%(dt,pointName))
                    if errorpoint:
                        errorData[dt] = errorpoint

                else:
                    print("请求接口%s返回数据为空!"%(self.url))
            if errorData:
                for i in errorData:
                    self.errors.append("项目id为%s的项目中掉线时间大于设定时间的虚拟点为%s"%(i,errorData[i]))
            BeopTools.raiseError(self.errors,self.testCaseID)
        else:
            print("执行时间未到！")


    def getdata(self,pointId,pointList):
        a = BeopTools()
        data = {"proj":pointId,"pointList":pointList}
        rv = False
        try:
            rv = a.postData(self.url,data,t=30)
        except:
            rv = rv
        return rv





    def tearDown(self):
        use1 = str((datetime.datetime.now() - self.start).seconds)
        use = use1 + "s"
        print("本次用例执行时间为%s" % use)
        self.now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Calc046('Test'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)