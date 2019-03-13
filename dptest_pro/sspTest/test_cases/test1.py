import time
#返回当前时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))











localtime = time.asctime( time.localtime(time.time()) )

print ("本地时间为 :", localtime)

print ("本地时间为 :", time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))