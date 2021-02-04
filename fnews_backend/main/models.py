from django.db import models

class TagText(models.Model):
    tag = models.CharField('Тег', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.tag


class Text(models.Model):
    name = models.CharField('Назва тексту', max_length=100, blank=True, null=True)
    text = models.TextField('Досліджуванний текст', blank=True, null=True)
    tag = models.ManyToManyField(TagText, verbose_name='Тег', blank=True, null=True)

    def __str__(self):
        return self.text


