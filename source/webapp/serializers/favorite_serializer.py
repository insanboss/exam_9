from rest_framework import serializers
from webapp.models import Photo

# photo = models.ImageField(null=False, blank=False, upload_to='photos', verbose_name='Фото')
#     sign = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
#     author_photo = models.ForeignKey(get_user_model(), related_name='photos_author',
#                                      on_delete=models.CASCADE, verbose_name='Автор', null=False, blank=False)
#     album = models.ForeignKey("webapp.Album", on_delete=models.CASCADE, related_name='photos',
#                               verbose_name='альбом', null=True, blank=True)
#     status


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo', 'author_photo', 'album', 'rating', 'status', 'created_at')
        read_only_fields = ('author_photo',)
