from django.db import models
from django.conf import settings
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=248,
                                   blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        MAX_SIZE = 512

        if self.image:
            with Image.open(self.image) as img:
                sz = img.size
                if sz[0] > MAX_SIZE or sz[1] > MAX_SIZE:
                    img = img.resize((MAX_SIZE, MAX_SIZE))
                    img.save(self.image.path)

