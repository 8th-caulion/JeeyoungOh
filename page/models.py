from django.conf import settings
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
