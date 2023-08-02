from django.db import models
from django.contrib.auth.models import User


class ArticleNew(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='article_new_object'
    )
    title = models.CharField(max_length=64)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    likes_user = models.ManyToManyField(
        to=User,
        blank=True
    )

    def __str__(self):
        return self.title

    def NewViewCount(self):
        self.views_count += 1
        self.save()
