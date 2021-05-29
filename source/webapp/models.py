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


class PhotoUser(BaseModel):
    photo = models.ForeignKey("webapp.Photo", on_delete=models.CASCADE, related_name="PhotoUser")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="PhotoUser")

    class Meta:
        verbose_name = 'Избранное(фото)'
        verbose_name_plural = 'Избранные(фото)'

    def __str__(self):
        return "Id photo: {}. User: {}".format(self.photo_id, self.user)


class Album(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Текст альбома')
    author_album = models.ForeignKey(get_user_model(), related_name='album_author',
                                     on_delete=models.CASCADE, verbose_name='Автор', null=False, blank=False)
    status = models.CharField(max_length=50, null=False,
                              blank=False,
                              choices=status_choices,
                              default='public', verbose_name='статус')

    def __str__(self):
        return "name album: {}. id album: {}".format(self.name, self.id)


class AlbumUser(BaseModel):
    album = models.ForeignKey("webapp.Album", on_delete=models.CASCADE, related_name="AlbumUser")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="AlbumUser")

    class Meta:
        verbose_name = 'Избранное(альбом)'
        verbose_name_plural = 'Избранные(альбом)'

    def __str__(self):
        return "Id album: {}. User: {}".format(self.album_id, self.user)
