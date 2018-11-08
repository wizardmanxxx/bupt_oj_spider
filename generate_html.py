import conf
import re


def html_generator(dic):
    ret = '<table border="1">'
    keys = sorted(dic.keys())
    for key in keys:
        list = dic[key]
        length = len(list)
        line_name = '<tr><td colspan="3" align="center">' + key + '</td></tr>'
        list2 = find_latest_submit(list)
        for index, sub in enumerate(list2):
            if sub is None:
                continue
            str1 = str(sub['submit_code'], encoding='gbk').replace('\r\n', '\n')
            pattern = re.compile(r'\n')
            line_count = len(pattern.findall(str1))
            # line_left = '<tr><td>' + sub['submit_id'] + '</td><td>' + sub[
            #     'submit_question'] + '</td><td>' + sub[
            #                 'submit_result'] + '</td></tr><tr><td colspan="3"><textarea rows="' + str(
            #     line_count + 1) + '" cols="100" >' + str1 + '</textarea></td></tr>'
            # line_left = '<tr><td>' + sub['submit_id'] + '</td><td>' + sub[
            #     'submit_question'] + '</td><td>' + sub[
            #                 'submit_result'] + '</td></tr><tr><td colspan="3"> '+str1+' </td></tr>'
            line_left = '<tr><td>' + sub['submit_id'] + '</td></tr><tr><td>' + sub[
                'submit_question'] + '</td></tr><tr><td>' + sub[
                            'submit_result'] + '</td></tr><tr><td ><textarea rows="' + str(
                line_count + 1) + '" cols="100" >' + str1 + '</textarea></td></tr>'

            line_name = line_name + line_left
        ret = ret + line_name
    with open('test.html', 'w') as f:
        f.write(ret)


def find_latest_submit(submit_list):
    list = [None, None, None, None, None]
    for index, li in enumerate(conf.question_list):
        latest = 0
        for sub_list in submit_list:
            if li in sub_list['submit_question']:
                if latest == 0:
                    list[index] = sub_list
                    latest = int(sub_list['submit_id'])
                elif int(sub_list['submit_id']) > latest:
                    list[index] = sub_list
                    latest = int(sub_list['submit_id'])
    return list
