from django.db import models
from django.contrib.auth.models import User
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.text
class Entry(models.Model):
    #学习到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
	
    def __str__(self):
        """返回模型字符串前50个字符"""
        if len(self.text) > 50:
            return self.text[:50]+'...'
        return self.text
			
			
		
# Create your models here.
