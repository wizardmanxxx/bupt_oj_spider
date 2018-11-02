from selenium import webdriver
import csv
from get_all_submits import *
import time

problem_url = conf.problem_url

exam_login_url = conf.exam_login_url
exam_pwd = conf.exam_pwd


def hust_login(driver, user, psw, cnt):
    # chromedriver_path = conf.chromedriver_path
    # 创建浏览器对象
    # driver = webdriver.Chrome(chromedriver_path)
    print(user)
    if cnt == 0:
        driver.get("http://10.112.143.110/loginpage.php")

    # 注销用户
    else:
        driver.find_element_by_xpath('//*[@id="profile"]').click()
        try:
            driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li/ul/li[5]/a').click()
        except:
            pass
        driver.get("http://10.112.143.110/loginpage.php")

        # 登录hust oj

    driver.find_element_by_name("user_id").send_keys(user)
    driver.find_element_by_name("password").send_keys(psw)
    driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[1]/button').click()
    alert = is_alert_present(driver)
    if alert:
        alert.accept()
        return None
    driver.get('http://10.112.143.110')
    # driver.get(conf.hustoj_login_address)
    # driver.find_element_by_name("password").send_keys(exam_pwd)
    # elem_sub2 = driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
    # elem_sub2.click()
    # # 判断是否登录成功
    # tmp = True
    # try:
    #     driver.find_element_by_xpath('//*[@id="profile"]')
    # except:
    #     tmp = False
    # if not tmp:
    #     alert = driver.switch_to_alert()
    #     print('user:'+user+'密码错误')
    #     time.sleep(2)
    #     alert.accept()
    #     return None

    # except:
    #     alert = driver.switch_to_alert()
    #     print('user:' + user + '密码错误')
    #     time.sleep(2)
    #     alert.accept()
    #     return None
    return driver


def get_usr_lst(dic):
    file = csv.reader(open('oj_user.csv', 'r', encoding='utf-8'))
    cnt = 0
    for f in file:
        if cnt == 0:
            cnt = cnt + 1
            continue

        cnt = cnt + 1
        dic[f[1]] = f[2]
    return dic


# 题目名称
def get_url(title):
    for k in problem_url:
        if k in title:
            return problem_url[k]
    return "ERROR"


def process(driver, id, submits_lst, count):
    # 获取账号密码
    user_dic = {}
    get_usr_lst(user_dic)
    try:
        pwd = user_dic[id]
    except:
        print('该用户不存在' + id)
        return 0
    driver = hust_login(driver, id, pwd, count)
    if driver is None:
        return 0
    # 提交每一道题
    for index, submit_dic in enumerate(submits_lst):
        # 获取题目
        title = submit_dic['submit_question']
        # 根据题目获取url
        submit_url = get_url(title)
        try:
            driver.get(submit_url)
        except:
            continue
        code = submit_dic['submit_code']
        set_text(code)

        text = driver.find_element_by_xpath('//*[@id="source"]/div[2]/div')
        ActionChains(driver).click(text).perform()
        # 粘贴
        driver.switch_to.active_element.send_keys(Keys.CONTROL, 'v')
        # 提交
        driver.find_element_by_xpath('//*[@id="Submit"]').click()
        if index != len(submits_lst) - 1:
            time.sleep(10)


def is_alert_present(driver):
    try:
        alert = driver.switch_to_alert()
        return alert
    except:
        return False


def test():
    dic = {}
    get_usr_lst(dic)
    # def hust_submit():
    # hust_login("2018110758", "2018110758")
