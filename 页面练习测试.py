from selenium import webdriver

# driver = webdriver.Ie()
# driver.get('http://www.baidu.com/')


#使用IE游览器
# import os
# from selenium import webdriver
# chromedriver = "C:\Program Files\internet explorer\iexplore.exe"
# os.environ["webdriver.Ie.driver"] = chromedriver
# driver =  webdriver.Ie(chromedriver)
# driver.get('http://www.baidu.com' )
# driver.quit()


#使用谷歌游览器
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

b = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
b.get('http://www.taobao.com' )
b.implicitly_wait(3)
b.find_element_by_link_text("亲，请登录").click()
acount1 = '18598274004'
pwd = 'ye13715119027'
# time.sleep(2)
user_ele = b.find_element_by_xpath('//*[@id="fm-login-id"]')
user_ele.send_keys(acount1)
pwd_ele = b.find_element_by_xpath('//*[@id="fm-login-password"]')
pwd_ele.clear()
pwd_ele.send_keys(pwd)
time.sleep(1)
but1= b.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(b).click_and_hold(but1).perform()#点击不放
ActionChains(b).move_to_element_with_offset(but1,300,0).perform()#右移300像素

b.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click() #点击登录
# time.sleep(3)
b.find_element_by_link_text('天猫超市').click()
b.switch_to.window(b.window_handles[1])
b.find_element_by_id('mq').send_keys('叶酸')
b.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button').click()

# b.back()
# b.quit()
