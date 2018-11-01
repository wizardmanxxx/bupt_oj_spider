    from selenium import webdriver
import time
import re
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys


def login():
    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # 创建浏览器对象
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("http://10.105.242.83/accounts/login/")
    cookie = driver.get_cookies()
    try:
        driver.find_element_by_id("id_username").send_keys("scsxuliutong")
        driver.find_element_by_id("id_password").send_keys("154639")
        elem_sub = driver.find_element_by_xpath('//*[@id="content_body"]/div/div/div[1]/form/button')
        elem_sub.click()
    except:
        print("登陆失败")
    return driver


def get_submit():
    driver.get("http://10.105.242.83/contest/430/submission/")
    pages = driver.find_element_by_xpath('//*[@id="wrapper"]/div/ul/li[1]').text.split(' ')[3]
    stu_submit = {}
    # 遍历所有页
    for page in range(1, 2):
        url = 'http://10.105.242.83/contest/430/submission/' + '?page=' + str(page) + '&'
        driver.get(url)
        entrys = 15
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

            if sub_user not in stu_submit:
                tmp = [dic]
                stu_submit[sub_user] = tmp
            else:
                stu_submit[sub_user].append(dic)
    return stu_submit


def add_code():
    for user_id in stu_submit.keys():
        for dic in stu_submit[user_id]:
            url = 'http://10.105.242.83/contest/430/submission/' + dic['submit_id']
            driver.get(url)
            textarea =  driver.find_element_by_id('code-text')
            textarea.get_attribute('innerHTML')
            code = driver.execute_script("return arguments[0].innerHTML", textarea)

            print(code)


if __name__ == "__main__":
    driver = login()
    stu_submit = get_submit()
    add_code()
    print('test')

# 获取新的页面快照
driver.save_screenshot("denglu.png")

# 打印网页渲染后的源代码
# print(driver.page_source)

# 获取当前页面Cookie
# print(driver.get_cookies())

# ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 输入框重新输入内容
# driver.find_element_by_id("kw").send_keys("test")

# 模拟Enter回车键
# driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
# driver.find_element_by_id("kw").clear()

# 生成新的页面快照
# driver.save_screenshot("test.png")

# 获取当前url
# print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()
