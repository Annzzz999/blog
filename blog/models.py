from django.conf import settings
from django.db import models
from django.utils import timezone


class Kategori(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Текст",max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Bluda1(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        kategori =models.ForeignKey(Kategori,  verbose_name="Категория",  on_delete=models.SET_NULL,  null=True)
        title = models.CharField("Название", max_length=200)
        text = models.TextField("Описание")
        created_date = models.DateTimeField("Дата начала",default=timezone.now)
        published_date = models.DateTimeField("Дата окончания",blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title




# Create your models here.
