import smtplib
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 


smtpObj = smtplib.SMTP_SSL("smtp.qq.com")
smtpObj.login("499908174@qq.com","zzokkzruycbobicd")
smtpObj.sendmail("499908174@qq.com","mapengfei@mail.nwpu.edu.cn","ddddfasdfa")
smtpObj.quit()
 
if __name__ == '__main__':
        fromaddr = '499908174@qq.com'
        password = 'zzokkzruycbobicd'
        toaddrs = ['dhgxwxb@163.com', '499908174@qq.com']
        
        m = MIMEMultipart()
        content = '请下载附件！'
        textApart = MIMEText(content)
        m.attach(textApart)
 
        # 湖北日报
        pdfFile = 'hubei_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)

        # 长江日报
        pdfFile = 'changjiang_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)

        m['Subject'] = '湖北新闻摘要'
        m['From'] = f'马鹏飞 <{fromaddr}>'
        m['To'] = f'许诺 <{toaddrs}>'
        m['Date']= time.strftime("%Y-%m-%d",time.localtime())
 
        try:
            server = smtplib.SMTP('smtp.qq.com')
            server.login(fromaddr,password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:',e) #打印错误
