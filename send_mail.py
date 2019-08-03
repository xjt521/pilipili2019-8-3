import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'pilipili.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自pilipili的测试邮件', 'xjt1223564154@sina.com', '1223564154@qq.com'
    text_content = '当html无效时使用此处内容进行替换'
    html_content = '<p>欢迎访问<a href="http://www.bilibili.com" target=blank>www.bilibili.com</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()