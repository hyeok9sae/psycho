from django.db import models

# # Create your models here.
# class SNSKeyword(models.Model):
#     id = models.IntegerField(primary_key=True)
#     keyword = models.CharField(max_length=30)
#     num = models.IntegerField(max_length=10, null=True)
#
#     def __str__(self):
#         return [self.id, self.keyword, self.num]
#
#
# class SNSContent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     content = models.CharField(max_length=500, null=True)
#
#     def __str__(self):
#         return [self.id, self.content]