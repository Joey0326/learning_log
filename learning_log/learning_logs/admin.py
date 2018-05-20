from django.contrib import admin
from learning_logs.models import Topic,Entry
#导入Topic
admin.site.register(Topic)
admin.site.register(Entry)
#让Django通过管理网站管理模型
# Register your models here.
