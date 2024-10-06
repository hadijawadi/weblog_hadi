from django.db import models



class Contact(models.Model):
    full_name = models.TextField(max_length=400)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.email
    
