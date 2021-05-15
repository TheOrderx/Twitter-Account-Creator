import json
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from smsactivateru import SmsTypes

import adb_controller as adb
import get_number as getnum
import gmail_reader as gr
import utils


# Import


def tel_mode(driver):
    # tel num
    country_code = SmsTypes.Country.RU
    while True:
        try:
            data = getnum.get_number(country_code)
            break
        except Exception as e:
            print(e)

    print("Select yapılıyor")
    Select(driver.find_elements_by_tag_name("select")[0]).select_by_value(
        getnum.parse_code(country_code))
    print("Telefon numarası")
    driver.find_elements_by_name("phone_number")[0].clear()
    driver.find_elements_by_name("phone_number")[0].send_keys(data[4])

    print(data)

    time.sleep(2)
    check_tel(driver, data[5])


def tel_mode_sign(driver):
    global number
    country_code = SmsTypes.Country.RU
    while True:
        try:
            data = getnum.get_number(country_code)
            break
        except Exception as e:
            print(e)
    print("Telefon numarası")
    number = data[1]
    driver.find_elements_by_tag_name("input")[1].clear()
    driver.find_elements_by_tag_name("input")[1].send_keys("+" + data[1])
    time.sleep(1.5)
        
    texts = driver.find_elements_by_class_name("css-1dbjc4n")[0].text
    if "Lütfen geçerli bir telefon numarası gir." in texts:
        data[5].cancel()
        tel_mode_sign(driver)
    else:
        print("Status: True")
        click_all(driver)
        check_tel_sign(driver, data[5])


def check_tel(driver, tel_data):
    texts = driver.find_elements_by_class_name("css-1dbjc4n")[0].text
    if "Please" in texts:
        tel_data.cancel()
        tel_mode(driver)
    else:
        driver.find_elements_by_class_name("css-18t94o4")[0].click()
        driver.find_elements_by_class_name("css-18t94o4")[4].click()
        time.sleep(1)
        if "önderilemiyor" in driver.find_elements_by_class_name("css-1dbjc4n")[0].text:
            print("ERROR!")
            exit()
        elif "limit" in driver.find_elements_by_class_name("css-1dbjc4n")[0].text:
            print("ERROR!")
            exit()
        else:
            get_tel_code(driver, tel_data)


def check_tel_sign(driver, tel_data):
    texts = driver.find_elements_by_class_name("css-1dbjc4n")[0].text
    if "Please" in texts:
        tel_data.cancel()
        tel_mode_sign(driver)
    else:
        driver.find_elements_by_class_name("css-901oao")[50].click()
        time.sleep(1)
        if "önderilemiyor" in driver.find_elements_by_class_name("css-1dbjc4n")[0].text:
            print("ERROR!")
        elif "limit" in driver.find_elements_by_class_name("css-1dbjc4n")[0].text:
            print("ERROR!")
        else:
            get_tel_code(driver, tel_data)


def get_tel_code(driver, tel_data):
    print("tel kodu alınıyor")
    driver.find_elements_by_tag_name("input")[0].clear()
    tel_data.was_sent()
    try:
        driver.find_elements_by_tag_name("input")[0].send_keys(tel_data.wait_code(timeout=20))
        driver.find_elements_by_class_name("css-901oao")[3].click()
        verify_code(driver)
    except:
        tel_data.cancel()
        driver.find_elements_by_class_name("css-901oao")[0].click()
        if jsondata["mailOrPhone"] == "Mail":
            tel_mode(driver)
        else:
            driver.find_elements_by_tag_name("input")[1].click()
            tel_mode_sign(driver)


def succes_acc(driver):
    global number
    time.sleep(3)
    driver.find_elements_by_class_name("css-16my406")[3].click()  # resim yükle
    time.sleep(2)
    try:
        biographs = open("biographs.txt", "r", encoding="utf8").read().split("\n\n\n\n\n")
        print(biographs[random.randint(0, len(biographs) - 1)])
        driver.find_elements_by_tag_name("textarea")[0].send_keys(
            biographs[random.randint(0, len(biographs) - 1)])  # Biyografi
    except Exception as e:
        print(e)

    time.sleep(1)
    driver.find_elements_by_class_name("css-16my406")[3].click()  # biyografi onay & geç
    time.sleep(1)
    driver.find_elements_by_class_name("css-16my406")[8].click()  # rehber geç
    time.sleep(1)
    driver.find_elements_by_class_name("css-16my406")[3].click()  # önerilenler geç
    time.sleep(1)
    driver.find_elements_by_class_name("css-16my406")[3].click()
    time.sleep(1)
    driver.find_elements_by_class_name("css-16my406")[8].click()
    time.sleep(1)
    #
    # url = "https://twitter.com/i/api/1.1/account/update_profile_image.json"
    #
    # payload = "image=" + str(open("Photos/data" + str(random.randint(0, 401)) + ".txt", "rb").read())
    #
    # cookies = ""
    # cookies += "_twitter_sess" + ":" + driver.get_cookie("_twitter_sess") + ";"
    # cookies += "auth_token" + ":" + driver.get_cookie("auth_token") + ";"
    # cookies += "ct0" + ":" + driver.get_cookie("ct0") + ";"
    # cookies += "twid" + ":" + driver.get_cookie("twid") + ";"
    # cookies += "mbox" + ":" + driver.get_cookie("mbox") + ";"
    #
    # headers = {
    #     "Connection": "keep-alive",
    #     "x-twitter-client-language": "en",
    #     "x-csrf-token": driver.get_cookie("ct0"),
    #     "sec-ch-ua-mobile": "?0",
    #     "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
    #                      "%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    #     "content-type": "application/x-www-form-urlencoded",
    #     "x-twitter-auth-type": "OAuth2Session",
    #     "Accept": "*/*",
    #     "Origin": "https://twitter.com",
    #     "Cookie": cookies
    # }
    #
    # response = requests.request("POST", url, data=payload, headers=headers)
    #
    # print(response.text)
    if jsondata["mailOrPhone"] == "Mail":
        utils.go_save(driver.find_elements_by_class_name("css-1dbjc4n")[59].text[1:], emailFull, passw)
    else:
        utils.go_save(driver.find_elements_by_class_name("css-1dbjc4n")[59].text[1:], number, passw)
    print("")


def get_code(driver):
    driver.find_elements_by_tag_name("input")[0].send_keys(gr.getmail())
    time.sleep(1)
    driver.find_elements_by_class_name("css-901oao")[2].click()
    verify_code(driver)


def verify_code(driver):
    time.sleep(2)
    texts = driver.find_elements_by_class_name("css-1dbjc4n")[0].text
    print(driver.find_elements_by_class_name("css-1dbjc4n")[0].text)
    if "number" in texts or "numara" in texts:
        # Error mode
        print("ERROR MODE")
        tel_mode(driver)
    elif "Sana bir kod gönderdik." in texts:
        print("WRONG CODE")
        driver.find_elements_by_tag_name("input")[0].clear()
        time.sleep(1)
        get_code(driver)
    elif "pass" in texts or "girmen" in texts:
        # not error mode
        print("NOT ERROR MODE")
        driver.find_elements_by_tag_name("input")[1].send_keys(passw)
        time.sleep(1.5)
        driver.find_elements_by_class_name("css-901oao")[2].click()
        time.sleep(1)
        succes_acc(driver)
    else:
        print("UNKNOWN")


def airplane_change():
    adb.change_airplane(True)
    time.sleep(4)
    adb.change_airplane(False)
    time.sleep(4)


def click_all(driver):  # sign up
    driver.find_elements_by_class_name("css-901oao")[2].click()
    driver.find_elements_by_class_name("css-901oao")[2].click()
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div["
        "2]/div[2]/div/div/div/div[5]/div").click()


data = open("settings.json", "r+", encoding="utf8")
jsondata = json.load(data)
data.close()

emailFull = ""
passw = ""
global_driver = ""
number = ""


def open_account():
    global passw, emailFull, global_driver
    email_end = jsondata["eMailEnd"]
    email = jsondata["email"]
    names = open("names.txt", "r", encoding='utf-8').read().split("\n")
    surname = open("surnames.txt", "r", encoding='utf-8').read().split("\n")
    passw = jsondata["password"]
    full_name = names[random.randint(0, len(names))] + " " + surname[random.randint(0, len(surname))]
    emailFull = email + "+" + str(random.randint(1, 99999)) + "@" + email_end
    options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path=jsondata["geckoPath"], options=options)
    global_driver = browser
    browser.implicitly_wait(10)
    browser.delete_all_cookies()

    browser.get("https://twitter.com/i/flow/signup")
    time.sleep(2)

    Select(browser.find_elements_by_tag_name("select")[0]).select_by_index('10')
    Select(browser.find_elements_by_tag_name("select")[1]).select_by_index('10')
    Select(browser.find_elements_by_tag_name("select")[2]).select_by_index('25')
    browser.find_elements_by_tag_name("input")[0].send_keys(full_name.lower())
    if jsondata["mailOrPhone"] == "Mail":
        browser.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div["
            "2]/div[2]/div/div/div[4]/span").click()
        time.sleep(3)
        click_all(browser)
        get_code(browser)
    else:
        tel_mode_sign(browser)

    browser.quit()


while True:
    try:
        airplane_change()
        open_account()
    except Exception as e:
        data = open("errors.txt", "a+")
        data.write(str(e))
        data.close()
        global_driver.quit()
        print(e)
        continue
