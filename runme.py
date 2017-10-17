from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time;

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = "xxxxx"
password = "xxxx"
# 输入SMTP服务器地址:
smtp_server = "xxxxx"
# 输入收件人地址:
to_addr = "xxxxx"

content = ["<html><body>"]
# 名字文件路径
names_file_path = "/Users/sun/Desktop/names.txt" # 源文件 1
names_file = open(names_file_path,"r")
content.append("<div align=""center"">""")
i = 0
all_people = 23
while True :
	line = names_file.readline()
	line = line.strip("\n")
	if line:
		if (i + 1) % 3 == 1:
			content.append("<br/>")
		content.append(line + "     ")
		i = i + 1
	else:
		break
real_people = i
content.insert(1, "<div align=""center""> 应到：" + str(all_people) + " | 实到：" + str(real_people) + "</div>")
content.append("<div align=""right""> 签到日期: " + time.strftime("%Y 年 %m 月 %d 日", time.localtime()) + "</div>")
content.append("</div></body></html>")

msg = MIMEText(str().join(content), 'html', 'utf-8')
msg['From'] = _format_addr('管理员 <%s>' % from_addr) # 在此处写入收件人名字
msg['To'] = _format_addr('所有人 <%s>' % to_addr)
msg['Subject'] = Header("今日签到情况 | " + time.strftime("%Y%m%d", time.localtime()), 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()