import smtplib
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

now_in_beijing = time.localtime(time.time()+28800)

if __name__ == '__main__':
        fromaddr = '499908174@qq.com'
        password = 'owdv{gp{gplschdc'
        password= ''.join(map(lambda x:chr(ord(x)-1),password))
        toaddrs = ['dhgxwxb@163.com', '499908174@qq.com']
        
        m = MIMEMultipart()
        content = '湖北新闻汇总(晚上):\n'
        content += f'暂无\n'
        content += '\n\n\n\n\n'
        content += f'还未抓取内容：\n'
        content += f'湖北新闻:https://news.hbtv.com.cn/cjy_hbxw/index.html\n'
        content += f'武汉新闻:http://www.whtv.com.cn/channel?id=25\n'
        content += f'中国新闻网｜湖北：http://www.hb.chinanews.com.cn/\n'
        content += f'荆楚网：http://wh.cnhubei.com\n'
        textApart = MIMEText(content)
        m.attach(textApart)
 

        m['Subject'] = '湖北新闻摘要(晚上)'
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



