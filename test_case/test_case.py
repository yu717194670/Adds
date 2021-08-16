'''
data = get_yaml(key="data.yaml文件中的名称")
'''

from typing import Mapping
from test_data.ChuShi_APP import ChuShi_APP
import pytest
import allure
from time import sleep
from test_data.read_yaml import get_yaml

driver = ChuShi_APP().driver
driver.implicitly_wait(15)

data = get_yaml(key="liuxing")

@pytest.mark.flaky(reruns=1, reruns_delay=2)
@pytest.mark.parametrize("name",data)
def test_name_click(name):
    sleep(2)
    print(name)
    allure.story("点击%s"%name)
    driver.find_element_by_xpath('//*[@text="%s"]'%name).click()
    if name == "加速完成":
        print("back退出")
        driver.back()