#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:email_demo.py
# @time:2020/5/10 9:21 上午

import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.abspath(os.path.dirname(__file__))
dir_path = os.path.join( current_path , '..', 'reports/禅道自动化测试报告V1.2.zip')

smtp_server = 'smtp.qq.com'  # 邮件服务器
smtp_sender = '289025994@qq.com'  # 邮箱名
smtp_senderpassword = 'wblkinjqbkfcbhfa'  # 授权码
smtp_receiver = '289025994@qq.com'  # 收件人
smtp_cc = '479262985@qq.com'  # 抄送人
smtp_subject = '自动化测试报告'  # 邮件主题
smtp_body = '来自Python邮件测试'  # 邮件正文
# smtp_file = dir_path


msg = MIMEText(smtp_body, "html", "utf-8")  # 邮件信息对象
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['cc'] = smtp_cc
msg['subject'] = smtp_subject
# msg = MIMEMultipart()
# with open(smtp_file, 'rb') as f:
#     mine = MIMEBase()

smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',')+smtp_cc.split(','), msg.as_string())

