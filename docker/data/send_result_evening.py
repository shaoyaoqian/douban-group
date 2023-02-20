import smtplib
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

now_in_beijing = time.localtime(time.time()+28800)
smtpObj = smtplib.SMTP_SSL("smtp.qq.com")
smtpObj.login("499908174@qq.com","zzokkzruycbobicd")
smtpObj.sendmail("499908174@qq.com","mapengfei@mail.nwpu.edu.cn","ddddfasdfa")
smtpObj.quit()
 
if __name__ == '__main__':
        fromaddr = '499908174@qq.com'
        password = 'zzokkzruycbobicd'
        toaddrs = ['dhgxwxb@163.com', '499908174@qq.com']
        
        m = MIMEMultipart()
        content = '湖北新闻汇总:\n'
        content += f'湖北日报:https://epaper.hubeidaily.net/pad/column/202302/11/node_01.html\n'
        content += '\n\n\n\n\n'
        content += f'还未抓取内容：\n'
        content += f'湖北新闻:https://news.hbtv.com.cn/cjy_hbxw/index.html\n'
        content += f'武汉新闻:http://www.whtv.com.cn/channel?id=25\n'
        textApart = MIMEText(content)
        m.attach(textApart)
 
        # 湖北日报
        pdfFile = 'hubei_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)
        pdfFile = 'hubei_daily_sorted.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)

        m['Subject'] = '湖北日报'
        m['From'] = f'马鹏飞 <{fromaddr}>'
        m['To'] = f'许诺 <{toaddrs}>'
        m['Date']= time.strftime("%Y-%m-%d",now_in_beijing)
 
        try:
            server = smtplib.SMTP('smtp.qq.com')
            server.login(fromaddr,password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:',e) #打印错误



