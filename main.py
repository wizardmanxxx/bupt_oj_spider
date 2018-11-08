from get_all_submits import *
import generate_html
import hust

if __name__ == "__main__":
    count = 0
    driver = login()
    # False not choose all students info,select students from conf.py info list (needed_list)
    stu_submit = get_submit(driver, False)
    add_code(driver, stu_submit)

    # generate_html.html_generator(stu_submit)

    for key in stu_submit.keys():
        hust.process(driver, key, stu_submit[key], count)
        count = 1

    driver.close()

# 获取新的页面快照
# driver.save_screenshot("denglu.png")

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
