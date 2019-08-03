from django.shortcuts import render,redirect
from database import models
from . import  forms
import  datetime
import  hashlib
from database.models import  OdinaryUsesr,Dynamics,Comments,Bookmarks,Barage,Friends,Thumbups
from django.conf import settings
# Create your views here.
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.OdinaryUsesr.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'log_reg/confirm.html', locals())

    c_time = confirm.create_at
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user_id.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'log_reg/confirm.html', locals())
    else:
        confirm.has_confirmed = True
        confirm.save()

        message = '感谢确认，请使用账户登录！'
        return render(request, 'log_reg/confirm.html', locals())

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = 'pilipili注册邮箱'

    text_content = '''欢迎来到pilipili
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>点我完成注册</a></p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def hash_code(s, salt='pilipili'):# hash加密，用于注册码
    h = hashlib.sha256()
    s=str(s)+salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()



def index(request):
    pass
    return render(request, 'log_reg/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.OdinaryUsesr.objects.get(user_id=username)
            except :
                message = '用户不存在！'
                return render(request, 'log_reg/login.html', locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'log_reg/login.html', locals())

            if user.user_password ==hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.user_id
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'log_reg/login.html', locals())
        else:
            return render(request, 'log_reg/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'log_reg/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('create_at')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'log_reg/register.html', locals())
            else:
                same_name_user = models.OdinaryUsesr.objects.filter(user_id=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'log_reg/register.html', locals())
                same_email_user = models.OdinaryUsesr.objects.filter(user_email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'log_reg/register.html', locals())
                now=datetime.datetime.now()
                new_user = models.OdinaryUsesr()
                new_user.user_id = username
                new_user.user_password= hash_code(password1)
                new_user.user_email = email
                new_user.create_at=now
                code = hash_code(new_user.user_id)
                new_user.code=code
                send_email(email, code)
                new_user.save()


                return redirect('/login/')
        else:
            return render(request, 'log_reg/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'log_reg/register.html', locals())



def logout(request):
        if not request.session.get('is_login', None):
            # 如果本来就未登录，也就没有登出一说
            return redirect("/login/")
        request.session.flush()
        return redirect("/login/")