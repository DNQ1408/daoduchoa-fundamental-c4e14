from gmail import GMail, Message
from random import *
import datetime




content1 = '''<p style="text-align: left;">Em ch&agrave;o thầy,</p>
<p style="text-align: center;">Em l&agrave; Đ&agrave;o Đức H&ograve;a lớp C4E. Em bị {{sick_ness}}. Em xin ph&eacute;p nghỉ học. :(</p>
<p style="text-align: left;">Học sinh,</p>
<p style="text-align: left;"><em><strong>H&ograve;a</strong></em></p>'''

content2 = '''<p style="text-align: left;">Em ch&agrave;o c&ocirc;,</p>
<p style="text-align: center;">Em l&agrave; Đ&agrave;o Đức H&ograve;a lớp C4E. Em bị {{sick_ness}}. Em xin ph&eacute;p nghỉ học. :(</p>
<p style="text-align: left;">Học sinh,</p>
<p style="text-align: left;"><em><strong>H&ograve;a</strong></em></p>'''

content3 = '''<p style="text-align: left;">Em ch&agrave;o anh,</p>
<p style="text-align: center;">Em l&agrave; Đ&agrave;o Đức H&ograve;a lớp C4E. Em bị {{sick_ness}}. Em xin ph&eacute;p nghỉ học. :(</p>
<p style="text-align: left;">Học sinh,</p>
<p style="text-align: left;"><em><strong>H&ograve;a</strong></em></p>'''

reason1 = 'phong'
reason2 = 'Trúng gió'
reason3 = 'ngủ dây muộn'

list_content = [content1, content2, content3]
list_reason = [reason1, reason2, reason3]

content_template = choice(list_content)
sickness = choice(list_reason)
content = content_template.replace('{{sick_ness}}', sickness)

gmail = GMail ('hoadd.20144@gmail.com','Hoa.2101')
msg = Message ('Nghi om',to='hoadd.20144@gmail.com', html= content)

cur_hour_7 = False
while not cur_hour_7:
    now = datetime.datetime.now()
    if now.hour >= 7:
        gmail.send(msg)
        cur_hour_7 = True
