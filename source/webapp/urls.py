from django.urls import path

from webapp.views import IndexPhotos
from webapp.views.albums import AlbumView
from webapp.views.photos import PhotoView, PhotoCreate, PhotoUpdate, PhotoDelete

app_name = 'photos'

urlpatterns = [
    path('', IndexPhotos.as_view(), name='index_photos'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreate.as_view(), name='photo_add'),
    path('photo/<int:pk>/update/', PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDelete.as_view(), name='photo_delete'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),

]
