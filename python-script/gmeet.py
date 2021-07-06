from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import schedule
from datetime import date
from datetime import datetime
import pymongo                  #pip install dnspython and pip install pymongo
from pymongo import MongoClient


#--------------- Selenium----------------------
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(options=chrome_options)
#----------------------------------------------
myclient = pymongo.MongoClient("mongodb+srv://---yourdbusername--:--yourdbpasword--@cluster0.lesxr.mongodb.net/gmeetDB")
mydb = myclient["gmeetDB"]
print(mydb.list_collection_names())
mycol = mydb["datas"]

# the main working of the programme
def automate(username,password,message,url,attendancetime,classtime):
    driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.246717123.657996969.1616252528-430727744.1616252528&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/label/input").send_keys(url)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button").click()
    time.sleep(15)
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div").click()
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span").click()


    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span").click()
    time.sleep(attendancetime)
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea").send_keys(message) 
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[2]/span").click()

    time.sleep(classtime)
    driver.quit()


#-------------------------------------------------------------------------------------------

# ---------------- Data -----------------------

for x in mycol.find():
    username=x['username']
    password=x['password']
    message=x['message']
    url=x['link']
    attendancetime=5
    classtime=100
    automate(username,password,message,url,attendancetime,classtime)