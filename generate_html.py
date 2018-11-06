def html_generator(dic):
    ret = '<table border="1"><tr><th>学号</th><th>提交id</th><th>题目名称</th><th>提交结果</th><th>提交代码</th></tr>'
    for key in dic.keys():
        list = dic[key]
        length = len(list)
        line_name = '<tr><td rowspan="' + str(length) + '">' + key + '</td>'

        for index, sub in enumerate(list):
            if index != 0:
                line_left = '<tr>'
            else:
                line_left = ''
            line_left = line_left + '<td>' + sub['submit_id'] + '</td><td>' + sub[
                'submit_question'] + '</td><td>'+sub['submit_result']+'</td><td><textarea rows="20" cols="100">' + str(sub[
                            'submit_code'], encoding='gbk') + '</textarea></td></tr>'
            line_name = line_name + line_left
        ret = ret + line_name
    with open('test.html', 'w') as f:
        f.write(ret)
