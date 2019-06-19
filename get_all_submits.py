from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import generate_html
import win32clipboard as w
import conf

import win32con


def login():
    chromedriver_path = conf.chromedriver_path
    # 创建浏览器对象
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(conf.login_address)
    cookie = driver.get_cookies()
    try:
        driver.find_element_by_id("id_username").send_keys(conf.id_username)
        driver.find_element_by_id("id_password").send_keys(conf.id_password)
        elem_sub = driver.find_element_by_xpath('//*[@id="content_body"]/div/div/div[1]/form/button')
        elem_sub.click()
    except:
        print("登陆失败")
    return driver


def get_submit(driver, is_all_stu=True):
    driver.get(conf.submit_address)
    pages = driver.find_element_by_xpath('//*[@id="wrapper"]/div/ul/li[1]').text.split(' ')[3]
    stu_submit = {}
    # 遍历所有页
    for page in range(1, 73):
        url = conf.submit_address + '?page=' + str(page) + '&'
        driver.get(url)
        entrys = 16
        # 遍历每页中的提交
        for entry in range(1, entrys):
            dic = {}
            try:
                sub_id = driver.find_element_by_xpath(
                    '// *[ @ id = "wrapper"] / div / table / tbody / tr[' + str(entry) + '] / td[1]').text
                dic['submit_id'] = sub_id
                sub_question = driver.find_element_by_xpath(
                    '//*[@id="wrapper"]/div/table/tbody/tr[' + str(entry) + ']/td[2]').text
                dic['submit_question'] = sub_question
                sub_result = driver.find_element_by_xpath(
                    '//*[@id="wrapper"]/div/table/tbody/tr[' + str(entry) + ']/td[3]').text
                dic['submit_result'] = sub_result
                sub_user = driver.find_element_by_xpath(
                    '//*[@id="wrapper"]/div/table/tbody/tr[' + str(entry) + ']/td[7]').text
            except:
                print('获取完毕')
                return stu_submit

            if not is_all_stu and sub_user not in conf.needed_stu:
                continue
            if sub_user not in stu_submit:
                tmp = [dic]
                stu_submit[sub_user] = tmp
            else:
                stu_submit[sub_user].append(dic)
    return stu_submit


def add_code(driver, stu_submit):
    for user_id in stu_submit.keys():
        for dic in stu_submit[user_id]:
            if dic is None:
                continue
            url = conf.submit_address + dic['submit_id']
            driver.get(url)
            # textarea =  driver.find_element_by_id('code-text')
            # textarea.get_attribute('innerHTML')
            # code = driver.execute_script("return arguments[0].innerHTML", textarea)
            # 鼠标模拟点击
            text = driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div[1]/pre/span/span')
            ActionChains(driver).click(text).perform()

            driver.switch_to.active_element.send_keys(Keys.CONTROL, 'a')
            driver.switch_to.active_element.send_keys(Keys.CONTROL, 'c')
            code = get_text()
            dic['submit_code'] = code


def pack_sub(stu_submit):
    for user_id in stu_submit.keys():
        latest = generate_html.find_latest_submit(stu_submit[user_id])
        stu_submit[user_id] = latest
    return stu_submit


def get_text():  # 读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def set_text(aString):  # 写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()
