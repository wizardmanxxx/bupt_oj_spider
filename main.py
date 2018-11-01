from selenium import webdriver


# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 创建浏览器对象
driver = webdriver.Chrome(chromedriver_path)

driver.get("http://10.105.242.83/accounts/login/")

cookie1 = driver.get_cookies()
driver.find_element_by_id("id_username").send_keys("scsxuliutong")
driver.find_element_by_id("id_password").send_keys("154639")
elem_sub = driver.find_element_by_xpath('//*[@id="content_body"]/div/div/div[1]/form/button')
elem_sub.click()

driver.get("http://10.105.242.83/contest/430/submission/")


# 获取新的页面快照
driver.save_screenshot("denglu.png")

# 打印网页渲染后的源代码
#print(driver.page_source)

# 获取当前页面Cookie
#print(driver.get_cookies())

# ctrl+a 全选输入框内容
#driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
#driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 输入框重新输入内容
#driver.find_element_by_id("kw").send_keys("test")

# 模拟Enter回车键
#driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
#driver.find_element_by_id("kw").clear()

# 生成新的页面快照
#driver.save_screenshot("test.png")

# 获取当前url
#print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()
