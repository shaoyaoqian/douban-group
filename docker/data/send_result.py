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
        content = '湖北新闻汇总:\n'
        content += f'湖北日报：https://epaper.hubeidaily.net/pad/column/202302/11/node_01.html\n'
        content += f'长江日报：http://cjrb.cjn.cn/html/2023-02/12/node_1.htm\n'
        content += f'中国青年报：http://zqb.cyol.com/html/2023-02/10/nbs.D110000zgqnb_01.htm\n'
        content += f'科技日报：http://digitalpaper.stdaily.com/http_www.kjrb.com/kjrb/html/2023-02/10/node_2.htm\n'
        content += '\n\n\n\n\n'
        content += '还未抓取内容：\n'
        content += '荆楚网：http://wh.cnhubei.com\n'
        content += '湖北网络广播电视台：https://news.hbtv.com.cn/cjy_hbxw/index.html\n'
        content += '极目新闻：http://www.ctdsb.net/\n'
        content += '中国新闻网｜湖北：http://www.hb.chinanews.com.cn/\n'
        content += '中国经济网：http://www.ce.cn/\n'
        content += '黄鹤云：http://www.whtv.com.cn/\n'
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

        # 长江日报
        pdfFile = 'changjiang_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)
        pdfFile = 'changjiang_daily_sorted.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)
        
        # 中国青年报
        pdfFile = 'youth_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)
        pdfFile = 'youth_daily_sorted.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)

        # 科技日报
        pdfFile = 'tech_daily.html'
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m.attach(pdfApart)
        pdfFile = 'tech_daily_sorted.html'
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



