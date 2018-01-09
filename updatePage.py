import pip
from subprocess import call
import datetime

start = datetime.datetime.now()
print("准备升级所有库！开始时间为：{}".format(start.strftime("%Y-%m-%d %X")))
for dist in pip.get_installed_distributions():
    try:
        call("pip install --upgrade " + dist.project_name, shell=True)
    except:
        print("升级库{}失败，请手动升级！".format(dist.project_name))
end = (datetime.datetime.now()-start).total_seconds()
print("升级所有库结束！消耗时间为：{}S".format(end))


