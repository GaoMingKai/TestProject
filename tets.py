from functools import wraps

# from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         '''''decorator'''
#         print('Calling decorated function...')
#         return func(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def example():
#     """Docstring"""
#     print('Called example function')
# print(example.__name__, example.__doc__)
#
# example()

import asyncio


# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
# import time
# from time import sleep
# from datetime import datetime
# import threading
# loac = threading.Lock()
# heartbeatdata = {}
# hearthread = []
# def test(name):
#     i = 0
#     while True:
#         time.sleep(10)
#         i+=1
#         if i>3:
#             break
# def test001():
#     t1 = threading.Thread(target=test,args=('111',),name = "test001")
#     t2 = threading.Thread(target=test,args=('222',),name = "test002")
#     t3 = threading.Thread(target=test,args=('333',),name = "test003")
#     t1.start()
#     t2.start()
#     t3.start()
#     if t1.name=="test001":
#         startHeartbeat(heatbeatFunc,t1)
#     if t2.name=="test002":
#         startHeartbeat(heatbeatFunc,t2)
#     if t3.name=="test003":
#         startHeartbeat(heatbeatFunc,t3)
#
#
#
def heatbeatFunc(name):
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sleep(1)
        if not name.is_alive():
            break
        print(name.name,now)



def startHeartbeat(func,name):
    try:
        threading.Thread(target = func,args=(name,)).start()
    except Exception as e:
        assert 0,"错误信息为%s"%e.__str__()




# kk = 1
# kk1 =2
# from datetime import datetime
# from time import sleep
# from interfaceTest import app
# import requests,json,threading
# screenwash = app.config["SCREENWASH"]
# def screeningWasher(CaseId,fails):
#     loaddata = globals()
#     log = CaseId+"SW"
#     copydata = "CopyData"
#     logdata = CaseId+"data"
#     if not loaddata.get(copydata,False):
#         loaddata[copydata] = screenwash
#     if loaddata[copydata] != screenwash:
#         if loaddata[copydata][log] != screenwash[log]:
#             loaddata[copydata] = screenwash
#     if screenwash[log]-1:
#         if loaddata.get(logdata,False):
#             if loaddata[logdata] == fails:
#                 screenwash[log]-= 1
#         else:
#             loaddata[logdata] = fails
#         return False
#     else:
#         del loaddata[logdata]
#         screenwash[log] = loaddata[copydata][log]
#         return True
#
#
# def heartbeatthread():
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     try:
#         threading.Thread(target=heatbeatFunc,args=(now,)).start()
#     except Exception as e:
#         print("错误信息：%s"%e.__str__())
#
#
# heartbeatthread()



# screenwash ={"Test":3,"Test1":2}

#
# def screeningWasher(CaseId,fails):
#     loaddata = globals()
#     log = CaseId+"SW"
#     copydata = "Copy"+CaseId
#     logdata = CaseId+"data"
#     if not loaddata.get(copydata,False):
#         loaddata[copydata] = screenwash[log]
#     if screenwash[log]-1:
#         if loaddata.get(logdata,False):
#             if loaddata[logdata] == fails:
#                 screenwash[log]-= 1
#         else:
#             loaddata[logdata] = fails
#         return False
#     else:
#         del loaddata[logdata]
#         screenwash[log] = loaddata[copydata]
#         return True
#
# def work():
#     num = 0
#     while True:
#         kk = screeningWasher("Test","test001")
#         num+=1
#         if kk:
#             print("正常！")
#             num = 0
#         else:
#             print("第%s次！"%num)




#work()

#
# from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
#
# class Chrom(Chrome):
#     pass
#
# driver = Chrom()
# driver.set_page_load_timeout(10)
# driver.get("http://www.baidu.com")
# if driver.find_elements_by_css_selector("#kw"):
#     driver.execute_script("window.close()")



# try:
#     try:
#         num,num1 = 1,"2"
#         num = num+num1
#     except:
#         assert 0,"错误数据001！"
# except:
#     assert 0,"错误信息001！"


# from interfaceTest.Methods.BeopTools import BeopTools
#
#
#
# a = BeopTools()
# kk = '''
# Traceback (most recent call last):
#   File "D:/Beop-OnlineTest/interfaceTest/tets.py", line 174, in <module>
#     num = num+num1
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "D:/Beop-OnlineTest/interfaceTest/tets.py", line 176, in <module>
#     assert 0,"错误数据001！"
# AssertionError: 错误数据001！
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "C:\Program Files (x86)\JetBrains\PyCharm 5.0.3\helpers\pydev\pydevd.py", line 2407, in <module>
#     globals = debugger.run(setup['file'], None, None, is_module)
#   File "C:\Program Files (x86)\JetBrains\PyCharm 5.0.3\helpers\pydev\pydevd.py", line 1798, in run
#     launch(file, globals, locals)  # execute the script
#   File "C:\Program Files (x86)\JetBrains\PyCharm 5.0.3\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
#     exec(compile(contents+"\n", file, 'exec'), glob, loc)
#   File "D:/Beop-OnlineTest/interfaceTest/tets.py", line 178, in <module>
#     assert 0,"错误信息001！"
# AssertionError: 错误信息001！
# '''
#
# cc = a.ErrorInfoAuto(kk)
# print(cc)
# test = '''
# {% for item in reportStruct%}
#             <tr style="background-color:{{backgroundColor}};">
#                 <td>{{item[0]}}</td>
#                 <td>{{item[1]}}</td>
#                 <td>{{item[2]}}</td>
#                 <td>{{item[3]}}</td>
#                 <td>{{item[4]}}</td>
#                 <td>{{item[5]}}</td>
#                 <!--<td>{{item[6]}}</td>-->
#                 <!--<td>{{item[7]}}</td>-->
#                 <!--<td>{{item[8]}}</td>-->
#
#
# '''
#
# kk = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
#
# cc = test % dict( reportStruct = kk)
#
# print(cc)
import unittest
from functools import wraps
#
# def getTest(method):
#     @wraps(method)
#     def begin(self,*args,**kwargs):
#         if getattr(self,"faile",False):
#             self.faile = "Test001"
#         return method(self,*args,**kwargs)
#     return begin
#
#
# class Test(object):
#     faile = "Test"
#     @getTest
#     def test(self):
#         if self.faile == "Test001":
#             print(self.faile)
#         else:
#             print("no")
#
# a = Test()
# a.test()



# class Tests(unittest.TestCase):
#     error = []
#
#     def setUp(self):
#         self.error = []
#     def tearDown(self):
#         pass
#
#     def Test(self):
#         self.error.append("Test001")
#         print(self.error)
#
# if __name__ == '__main__':
#     while 1:
#         suit = unittest.TestSuite()
#         suit.addTest(Tests("Test"))
#         run = unittest.TextTestRunner()
#         res = run.run(suit)
#         print(res)

from interfaceTest import app
import datetime
from threading import Lock
import threading,json
lock = Lock()
screenwash = app.config["SCREENWASH"]
copyscreenwash = json.dumps(screenwash)


def screeningWasher(CaseId,fails):
    if lock:
        with lock:
            now = datetime.datetime.now()
            loaddata = globals()
            global screenwash
            log = CaseId+"SW"
            logdata = CaseId+"data"
            if screenwash[log]-1:
                if loaddata.get(logdata,False):
                    if fails in loaddata[logdata]:
                        if (now-loaddata[logdata].get(fails)).total_seconds()/60>5:
                            del loaddata[logdata]
                            screenwash[log] = json.loads(copyscreenwash)[log]
                        else:
                            screenwash[log]-= 1
                else:
                    loaddata[logdata] = {fails:now}
                return False
            else:
                del loaddata[logdata]
                screenwash[log] = json.loads(copyscreenwash)[log]
                return True

while True:
    CaseId = "Base002"
    error = "Test001"
    error1 = "Test002"
    kk = screeningWasher(CaseId,error)
    print(kk)


















