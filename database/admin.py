from django.contrib import admin
from database.models import  OdinaryUsesr,Dynamics,Comments,Bookmarks,Barage,Friends,Thumbups
# Register your models here.

class OdinaryUserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_email',)
    search_fields = ('user_id', 'user_email',)
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('user_id','user_password','user_email',)


class DynamicsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'author_id','content',)
    search_fields = ('post_title', 'author_id')
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id', 'post_title', 'content',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author_id','post_id','content',)
    search_fields = ('author_id', 'post_id','content,')
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id', 'post_id', 'content',)
class BookmarksAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'post_id', 'tag','url',)
    search_fields = ('author_id',)
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id', 'post_id', 'url','tag',)

class BarageAdmin(admin.ModelAdmin):
    list_display = ('author_id','video_id','barage_content',)
    search_fields = ('author_id','video_id',)
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id', 'video_id','barage_content',)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('author_id','friend_id','friend_type',)
    search_fields = ('author_id',)
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id','friend_id','friend_type',)
class ThumbupsAdmin(admin.ModelAdmin):
    list_display = ('author_id',)
    search_fields = ('author_id',)
    list_filter = ('create_at',)
    date_hierarchy = 'create_at'
    ordering = ('-create_at',)
    fields = ('author_id', )



admin.site.register(OdinaryUsesr,OdinaryUserAdmin)
admin.site.register(Dynamics,DynamicsAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Bookmarks,BookmarksAdmin)
admin.site.register(Barage,BarageAdmin)
admin.site.register(Friends,FriendsAdmin)
admin.site.register(Thumbups,ThumbupsAdmin)
