from django.contrib.auth import get_user_model
from django.db import models

status_choices = [('private', 'приватный'), ('public', 'публичный')]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Photo(BaseModel):
    photo = models.ImageField(null=False, blank=False, upload_to='photos', verbose_name='Фото')
    sign = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    author_photo = models.ForeignKey(get_user_model(), related_name='photos_author',
                                     on_delete=models.CASCADE, verbose_name='Автор', null=False, blank=False)
    album = models.ForeignKey("webapp.Album", on_delete=models.CASCADE, related_name='photos',
                              verbose_name='альбом', null=True, blank=True)
    status = models.CharField(max_length=50, null=False,
                              blank=False,
                              choices=status_choices,
                              default='public', verbose_name='статус')


class Album(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Текст альбома')
    author_album = models.ForeignKey(get_user_model(), related_name='album_author',
                                     on_delete=models.CASCADE, verbose_name='Автор', null=False, blank=False)
    status = models.CharField(max_length=50, null=False,
                              blank=False,
                              choices=status_choices,
                              default='new', verbose_name='статус')
    status = models.CharField(max_length=50, null=False,
                              blank=False,
                              choices=status_choices,
                              default='public', verbose_name='статус')
