import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global mail_host
    global mail_password

    send_user = '13020207396@163.com'
    mail_host = 'smtp.163.com'
    mail_password = 'GJXGKCTLDJNORFUT'

    def send_email(self, user_list, sub, content):
        user = "13020207396" + "<" + send_user + ">"
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = user
        message['To'] = ";".join(user_list)
        message['Subject'] = sub

        server = smtplib.SMTP()
        server.connect(host=mail_host)
        server.login(send_user, mail_password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num

        pass_result = '%.2f%%' % (pass_num / count_num * 100)
        fail_result = '%.2f%%' % (fail_num / count_num * 100)
        user_list = ['qp10161118@163.com', '1617491825@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
            count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_email(user_list, sub=sub, content=content)


if __name__ == '__main__':
    SendEmail().send_main([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])
