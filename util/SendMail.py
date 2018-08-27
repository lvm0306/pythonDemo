# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


class MailUtil():
    def __init__(self, content, subject):
        self.content = content
        self.subject = subject

    def sendMail(self):
        from_addr = '18545156106@163.com'
        password = 'shi123456'
        # 输入SMTP服务器地址:18545156106
        smtp_server = 'smtp.163.com'
        # 输入收件人地址:
        to_addr = 'ivm0306@163.com'

        msg = MIMEText(self.content, 'plain', 'utf-8')
        msg['From'] = "18545156106@163.com"
        msg['To'] = "ivm0306@163.com"
        msg['Subject'] = self.subject

        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def sendMailToOne(self,senter,reciver,reciver_stmp,stmp_psw):
        #设置发送人，收件人，stmp密码,stmp 服务器地址
        from_addr = senter
        to_addr = reciver
        password = stmp_psw
        smtp_server = reciver_stmp

        #设置msg
        msg = MIMEText(self.content, 'plain', 'utf-8')
        msg['From'] =from_addr
        msg['To'] =to_addr
        msg['Subject'] = self.subject

        #开始发送
        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


# from_addr = '18545156106@163.com'
# password = 'shi123456'
# # 输入SMTP服务器地址:18545156106
# smtp_server = 'smtp.163.com'
# # 输入收件人地址:
# to_addr = 'ivm0306@163.com'
#
# msg = MIMEText('对不起 我爱你', 'plain', 'utf-8')
# msg['From'] = "18545156106@163.com"
# msg['To'] = "ivm0306@163.com"
# msg['Subject'] = "this is my love for you "
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
