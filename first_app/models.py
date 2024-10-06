from django.db import models



class CreatePost(models.Model):
    title = models.TextField(max_length=1000)
    body = models.TextField(max_length=10000)
    thumbnail = models.ImageField(upload_to='images/' ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




    def __str__(self) -> str:
        return self.title[:40]
