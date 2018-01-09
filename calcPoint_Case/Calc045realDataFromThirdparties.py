__author__ = 'kirry'
import datetime,time
from interfaceTest import app
from interfaceTest.Methods.BeopTools import BeopTools
import unittest,json


muitTime = None
class Calc045(unittest.TestCase):
    testCaseID = 'Calc045'
    projectName = ""
    serverips = {"国服":app.config["SERVERIP"],"微软云美服":app.config["SERVERIP_ALL"]["微软云美服"]}
    buzName = '检查原始数据是否实时更新'
    projectId = {"MiamiRcc":674,"126 Church Street Parramatta":491,"开能环保":396,"和黄药业":374,'天津安捷':672}#"荣信钢铁":303,
    #projectId = {"和黄药业":374}
    AmericaId = [674]
    deltime = {"荣信钢铁":0,"MiamiRcc":-13,"126 Church Street Parramatta":3,"开能环保":0,"和黄药业":0,'天津安捷':0}


    def setUp(self):
        self.errors = []
        self.start = datetime.datetime.now()
        self.startime = self.start-datetime.timedelta(minutes = 20)

    def Test(self):
        for Id in self.projectId:
            url = "http://%s/admin/dataPointManager/search/"
            data = json.dumps({"projectId":"%(Id)s","text":None,"isAdvance":False,"order":"desc",
                           "isRemark":False,"flag":0,"starred":"","page_size":200,"current_page":1,"item":"time",})
            if self.deltime[Id] >= 0:
                now = datetime.datetime.now()+datetime.timedelta(hours = self.deltime[Id])
            else:
                now = datetime.datetime.now()-datetime.timedelta(hours = abs(self.deltime[Id]))

            data = json.loads(data%dict(Id = self.projectId[Id]))

            url = url % self.serverips["国服"] if self.projectId[Id] not in self.AmericaId else url % self.serverips["微软云美服"]

            rv = self.getData(url,data)

            if rv and isinstance(rv,list):
                rv = [(rv.get("pointname"),datetime.datetime.strptime(rv.get("time"),"%Y-%m-%d %H:%M"))
                      for rv in rv]
                pointName = []
                for rt in rv:
                    if rt[-1] > now:
                        dtime = (rt[-1]-now).total_seconds()/60
                    else:
                        dtime = (now-rt[-1]).total_seconds()/60
                    if dtime/60>24:
                        print("项目%s,有点掉线时间超过24小时！"%Id)
                        break
                    else:
                        if dtime > 30:
                            pointName.append(rt)
                if pointName.__len__() > 20:
                    self.errors.append("项目%s原始数据掉线数量超过20个！"%Id)
            else:
                assert 0,"请求接口%s,请求数据为%s返回数据为空！"%(url,data)
        BeopTools.raiseError(self.errors,self.testCaseID)






    def getData(self,url,data):
        try:
            rv = BeopTools.postJsonToken(url,data,60)
        except:
            assert 0,"请求接口%s超时60秒，请检查接口或数据是否正确！"%url
        return rv.get("list",False)






    def tearDown(self):
        use1 = str((datetime.datetime.now() - self.start).seconds)
        use = use1 + "s"
        print("本次用例执行时间为%s" % use)
        self.now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Calc045('Test'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)