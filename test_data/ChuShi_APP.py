#coding:utf-8
'''
path="本地apk路径"
appPackage="apk包名"
appActivity="apk Acticity"
deviceName="所需执行的设备名称"
'''

from appium import webdriver
import time
from test_data.SingletonPattern import singleton
from test_data.packagename import packagename
from test_data.packageActivity import packageActivity
@singleton
class ChuShi_APP():
    def __init__(self,path="/Users/yu_wenbin/Downloads/ctslink-t26-A0-vc1-vn1.0.605.apk",
                 appPackage=packagename()["changkuailian"],
                 appActivity=packageActivity()["changkuailian"],
                 deviceName="50b0e7d7"):

        desired_capadilities = {}
        # 手机操作系统
        desired_capadilities['platformName'] = 'Android'
        # 手机操作系统的版本
        # desired_capadilities['platformVersion'] = '5'
        # 使用的手机设备名称
        desired_capadilities['deviceName'] = deviceName
        # 本地绝对路径
        desired_capadilities['ap']= path
        # 重置应用
        desired_capadilities['noReset'] = True
        # 使用Unicode输入法。默认值为false
        desired_capadilities['unicodeKeyboard'] = True
        # 重置输入法到原有状态
        desired_capadilities['resetKeyboard'] = True
        # Activity的名字是指从你的包中所要的Android acticity
        desired_capadilities['appActivity'] = appActivity
        desired_capadilities['appPackage'] = appPackage

        desired_capadilities['automationName'] = 'UiAutomator2'
        print(desired_capadilities)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capadilities)
        time.sleep(5)

    def QuitApp(self):
        self.driver.quit()
    def LaunchApp(self):
        self.driver.launch_app()
    def CloseApp(self):
        self.driver.close_app()