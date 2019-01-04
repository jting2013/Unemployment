from selenium import webdriver
import time
import re
from datetime import datetime as dt
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config import *


import os
desktop = os.path.expanduser("~/Desktop")

path = desktop + r"/chromedriver.exe"
website = 'https://uionline.detma.org/Claimant/Core/Login.ASPX'
browser = webdriver.Chrome(path)
browser.set_page_load_timeout(10)
browser.get(website)

browser.find_element_by_id('ctl00_ctl00_cphMain_cphMain_chkWarning').click()

userSSN = 'ctl00_ctl00_cphMain_cphMain_txtSSN1'
confirmSSN = 'ctl00_ctl00_cphMain_cphMain_txtConfirmSSN1'


browser.find_element_by_id(userSSN).send_keys(SSN)
browser.find_element_by_id(confirmSSN).send_keys(SSN)
nextbtn = 'ctl00_ctl00_cphMain_cphMain_btnNext'
browser.find_element_by_id(nextbtn).click()
wait = WebDriverWait(browser, 10)

pwbox = 'ctl00_ctl00_cphMain_cphMain_txtClaimantPwd'

loginBtn = 'ctl00_ctl00_cphMain_cphMain_btnUIOnlineLogin'

browser.find_element_by_id(pwbox).send_keys(pwSSN)
browser.find_element_by_id(loginBtn).click()
wait = WebDriverWait(browser, 10)


requestID = 'ctl00_ctl00_cphMain_cphMain_lnkRqstBenefits'
browser.find_element_by_id(requestID).click()

WebDriverWait(browser, 5)
requestBtn = 'ctl00_ctl00_cphMain_cphMain_btnRequestBenefits'
browser.find_element_by_id(requestBtn).click()

WebDriverWait(browser, 5)
confirmBtn = 'ctl00_ctl00_cphMain_cphMain_btnConfirm'
browser.find_element_by_id(confirmBtn).click()

WebDriverWait(browser, 5)

# selecting yes which is "_0" and no "_1" to the questions
firstQuestion = 'ctl00_ctl00_cphMain_cphMain_radDidWork_1'
secondAQuestion = 'ctl00_ctl00_cphMain_cphMain_radOfferedEmployment_1'
secondBQuestion = 'ctl00_ctl00_cphMain_cphMain_radDischarged_1'
thirdQuestion = 'ctl00_ctl00_cphMain_cphMain_radReceivedIncome_1'
fourthWorkQuestion = 'ctl00_ctl00_cphMain_cphMain_radAbleToWork_0'
fourthAvailQuestion = 'ctl00_ctl00_cphMain_cphMain_radAvailableToWork_0'
fourthLookQuestion = 'ctl00_ctl00_cphMain_cphMain_radLookForWork_0'

questions = [firstQuestion, secondAQuestion, secondBQuestion, thirdQuestion,
             fourthWorkQuestion, fourthAvailQuestion, fourthLookQuestion]

for question in questions:
    browser.find_element_by_id(question).click()

WebDriverWait(browser, 5)
nextQuestion = 'ctl00_ctl00_cphMain_cphMain_btnNext'
browser.find_element_by_id(nextQuestion).click()

WebDriverWait(browser, 5)
informationUnderstand = 'ctl00_ctl00_cphMain_cphMain_chkAcknowledge'
browser.find_element_by_id(informationUnderstand).click()

WebDriverWait(browser, 5)
nextUnderstand = 'ctl00_ctl00_cphMain_cphMain_btnRegularWSNext'
browser.find_element_by_id(nextUnderstand).click()

browser.maximize_window()
WebDriverWait(browser, 10)
##select = Select(browser.find_element_by_id('ctl00_ctl00_cphMain_cphMain_ddlHowmanyDays'))
##select.select_by_visible_text('3')
browser.find_element_by_xpath('//*[@id="ctl00_ctl00_cphMain_cphMain_ddlHowmanyDays"]/option[5]').click()
time.sleep(3)

searchMethod1 = 'ctl00_ctl00_cphMain_cphMain_chkWorkSrcAct_1'
searchMethod12 = 'ctl00_ctl00_cphMain_cphMain_chkWorkSrcAct_12'
searchMethod14 = 'ctl00_ctl00_cphMain_cphMain_chkWorkSrcAct_14'

searchMethods = [searchMethod1, searchMethod12, searchMethod14]

for search in searchMethods:
    browser.find_element_by_id(search).click()

nextSerach = 'ctl00_ctl00_cphMain_cphMain_btnWorkQuestionnaireNext'
browser.find_element_by_id(nextSerach).click()


addBtn = 'ctl00_ctl00_cphMain_cphMain_btnWorkSearchLogAdd'

dateField = 'ctl00_ctl00_cphMain_cphMain_txtDate'
typeDropDwn = 'ctl00_ctl00_cphMain_cphMain_ddlType'
typeValue = 'EMPA'
employerField = 'ctl00_ctl00_cphMain_cphMain_txtEmployerAgencyNA'
nameField = 'ctl00_ctl00_cphMain_cphMain_txtPersonContacted'
contactDropDwn = 'ctl00_ctl00_cphMain_cphMain_ddlContactmethod'
contactValue = 'WSTE'
websiteField = 'ctl00_ctl00_cphMain_cphMain_txtContactInformation'
titleField = 'ctl00_ctl00_cphMain_cphMain_txtTypeofWork'
resultDropDwn = 'ctl00_ctl00_cphMain_cphMain_ddlResults'
resultValue = 'NORS'

submitBtn = 'ctl00_ctl00_cphMain_cphMain_btnAddWSLDetailsSubmit'

util = open('job.json', 'r')
re_util = json.load(util)
util.close()


for re_u in re_util:
    browser.find_element_by_id(addBtn).click()
    WebDriverWait(browser, 5)
    browser.find_element_by_id(dateField).send_keys(re_u['Date'])
    select = Select(browser.find_element_by_id(typeDropDwn))
    select.select_by_value(typeValue)
    browser.find_element_by_id(employerField).send_keys(re_u['Name'])
    browser.find_element_by_id(nameField).send_keys('N/A')
    select = Select(browser.find_element_by_id(contactDropDwn))
    select.select_by_value(contactValue)
    website = 'www.' + re_u['Contact Information'] + '.com'
    browser.find_element_by_id(websiteField).send_keys(website)
    browser.find_element_by_id(titleField).clear()
    browser.find_element_by_id(titleField).send_keys(re_u['Type of Work'])
    select = Select(browser.find_element_by_id(resultDropDwn))
    select.select_by_value(resultValue)
    browser.find_element_by_id(submitBtn).click()


completeBtn = 'ctl00_ctl00_cphMain_cphMain_btnWorkSearchLogSubmit'
browser.find_element_by_id(completeBtn).click()
