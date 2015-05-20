from django.contrib import admin
from common_lib.users.models import User
from index.models import Page, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Page)
admin.site.register(Comment)
