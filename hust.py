from selenium import webdriver
import csv
from get_all_submits import *

problem_url = {"新计算器二": "http://10.112.143.110/submitpage.php?cid=1003&pid=0&langmask=262140",
           "双11优惠": "http://10.112.143.110/submitpage.php?cid=1003&pid=1&langmask=262140",
           "数字统计二": "http://10.112.143.110/submitpage.php?cid=1003&pid=2&langmask=262140",
           "打印图形四": "http://10.112.143.110/submitpage.php?cid=1003&pid=3&langmask=262140",
           "个位数": "http://10.112.143.110/problem.php?cid=1003&pid=4"}

exam_login_url = "http://10.112.143.110/contest.php?cid=1007"
exam_pwd = "123"

def hust_login(user, psw):
    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # 创建浏览器对象
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("http://10.112.143.110/loginpage.php")
    cookie = driver.get_cookies()
    try:
        driver.find_element_by_name("user_id").send_keys(user)
        driver.find_element_by_name("password").send_keys(psw)
        elem_sub = driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[1]/button')
        elem_sub.click()
        driver.get("http://10.112.143.110/contest.php?cid=1007")
        driver.find_element_by_name("password").send_keys(exam_pwd)
        elem_sub2 = driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
        elem_sub2.click()

    except:
        print("登陆失败")
    return driver

def get_usr_lst(dic):
    file = csv.reader(open('oj_user.csv', 'r', encoding='utf-8'))
    cnt = 0
    for f in file:
        if cnt == 0:
            cnt = cnt+1
            continue

        cnt = cnt+1
        dic[f[1]] = f[2]
        #print(f[1])
        #print(dic[f[1]])
        #print("-----------------------------------------------------")
    return dic


# 题目名称
def get_url(title):
    for k in problem_url:
        if k in title:
            return problem_url[k]
    return "ERROR"


def process(id, submits_lst):
    # 获取账号密码
    user_dic = {}
    get_usr_lst(user_dic)
    pwd = user_dic[id]
    driver = hust_login(id, pwd)
    # 提交每一道题
    for submit_dic in submits_lst:
        # 获取题目
        title = submit_dic['question']
        # 根据题目获取url
        submit_url = get_url(title)

        driver.get(submit_url)
        code = submit_dic['submit_code']
        set_text(code)

        text = driver.find_element_by_xpath('//*[@id="source"]/div[2]/div')
        ActionChains(driver).click(text).perform()
        # 粘贴
        driver.switch_to.active_element.send_keys(Keys.CONTROL, 'v')
        # 提交
        elem_sub = driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
        elem_sub.click('//*[@id="Submit"]')






def test():
    dic = {}
    get_usr_lst(dic)
    #def hust_submit():
    #hust_login("2018110758", "2018110758")


