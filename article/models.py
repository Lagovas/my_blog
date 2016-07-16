from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

#создаем модель который будет отвечать за комментарии
class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(verbose_name="Comments text")
    article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
