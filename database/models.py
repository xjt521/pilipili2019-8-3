from django.db import models
import  datetime

# Create your models here.
class OdinaryUsesr(models.Model):
    user_id=models.CharField(max_length=128,unique=True)
    user_password = models.CharField(max_length=256)
    create_at = models.DateTimeField(null=True,auto_now=True)
    update_at = models.DateTimeField(null=True)
    user_email=models.EmailField(unique=True)
    has_confirmed=models.BooleanField(default=False)
    code = models.CharField(max_length=256,null=True)


    def __str__(self):
     return u'%s ' % (self.user_id)

class Dynamics(models.Model):
    post_title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    author_id=models.ForeignKey(OdinaryUsesr,on_delete=models.CASCADE)
    def __str__(self):
     return u'%s %s' % (self.post_title,self.content)

class Comments(models.Model):
    author_id = models.ForeignKey(OdinaryUsesr, on_delete=models.CASCADE)
    post_id=models.IntegerField()
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    content = models.CharField(max_length=500)
    def __str__(self):
     return u'%s %s' % (self.post_id,self.content)

class Bookmarks(models.Model):
    author_id = models.ForeignKey(OdinaryUsesr, on_delete=models.CASCADE)
    post_id = models.IntegerField()
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    url=models.URLField()
    tag=models.CharField(max_length=100)
    def __str__(self):
     return u'%s %s' % (self.tag,self.url)

class Barage(models.Model):
    author_id = models.ForeignKey(OdinaryUsesr, on_delete=models.CASCADE)
    video_id = models.IntegerField()
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    barage_time=models.DateTimeField()
    barage_size=models.IntegerField()
    barage_font=models.IntegerField()
    barage_loc=models.CharField(max_length=50)
    barage_content=models.CharField(max_length=100)

    def __str__(self):
        return u'%s %s %s' % (self.author_id, self.video_id,self.barage_content)


class Friends(models.Model):
    author_id=models.ForeignKey(OdinaryUsesr,related_name='Friend_author_id',on_delete=models.CASCADE)
    friend_id=models.ForeignKey(OdinaryUsesr,related_name='Friend_friend_id',on_delete=models.CASCADE)
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    friend_type=models.IntegerField()

    def __str__(self):
        return u'%s %s %s' % (self.author_id, self.friend_id, self.friend_type)

class Thumbups(models.Model):
    create_at = models.DateTimeField(null=True, auto_now=True)
    update_at = models.DateTimeField(null=True)
    author_id = models.ForeignKey(OdinaryUsesr, on_delete=models.CASCADE)
    post_id=models.IntegerField()
    def __str__(self):
        return u'%s ' % (self.author_id)
"""class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.ForeignKey('OdinaryUsesr', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user_id + ":   " + self.code"""

