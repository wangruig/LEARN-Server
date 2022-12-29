import smtplib
from email.mime.text import MIMEText

#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com' 
mail_user = ''
password = ''

#邮件发送方邮箱地址
sender = 'wang_ruiguo1012@163.com'
#邮件接受方邮箱地址
receivers = ['wangrg@dchealth.com']

message = MIMEText('相关程序重启失败，请尽快上线解决！','plain','utf-8')
#邮件主题       
message['Subject'] = 'Error! 十万火急！程序崩了！' 
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(mail_host, 25)
    #登录到服务器
    smtpObj.login(mail_user, password) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
