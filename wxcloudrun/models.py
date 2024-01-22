from datetime import datetime

from django.db import models


# Create your models here.

class wheatinfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    母本 = models.CharField(max_length=255)
    父本 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'wheatinfo' 
    

# class Counters(models.Model):
#     id = models.AutoField
#     count = models.IntegerField(max_length=11, default=0)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = 'wheatinfo'  # 数据库表名
