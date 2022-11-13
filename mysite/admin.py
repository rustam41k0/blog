from django.contrib import admin

# Register your models here.
from mysite.models import *


class PostsAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category)
admin.site.register(Comments)
