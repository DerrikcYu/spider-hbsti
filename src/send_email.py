import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

SEND_MAIL=True

class SendMailToMe(object):
    def process_item(self,item):
        content_html = ''
        for p in item['noticeContent']:
            content_html = content_html + '<p>' + p + '</p>'
        if SEND_MAIL:
            sender = "yancy2017@163.com"
            password = "BJT5dtpivf7XB4XW"
            receiver = '1347610023@qq.com'
            title=item['noticeTitle']
            content="""
                    <p>%s<p>
                    <p><a href="%s">%s</a></p>
                    <p>%s</p>
                    %s
                    """%(item['noticeType'], item['noticeUrl'], item['noticeTitle'], item['noticeDate'], content_html)
            # print('邮件内容',content)
            ret=self.sendMail(sender,password,receiver,title,content)
            print('================',ret)
            if ret:
                print("邮件发送成功")
            else:
                print("邮件发送失败")
            pass
    #=========================================================================
    def sendMail(self,sender,password,receiver,title,content):
        ret=True
        try:
            msg=MIMEText(content,'html','utf-8')
            msg['From']=formataddr(['', sender])
            msg['To'] = formataddr(['',receiver])
            msg['Subject'] = "科技情报动态:" + title
            server=smtplib.SMTP('smtp.163.com',25)
            print(sender,password)
            server.login(sender,password)
            server.sendmail(sender,[receiver],msg.as_string())
            server.quit()
        except Exception:
            ret= False
        return ret