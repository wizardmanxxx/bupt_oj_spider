from get_all_submits import *
import generate_html
import hust

if __name__ == "__main__":
    count = 0
    driver = login()
    # False ，dont choose all students info,select students from conf.py info list (needed_list)
    stu_submit = get_submit(driver)
    stu_submit = pack_sub(stu_submit)
    add_code(driver, stu_submit)

    generate_html.html_generator(stu_submit)

    # for key in stu_submit.keys():
    #     hust.process(driver, key, stu_submit[key], count)
    #     count = 1

    driver.close()
