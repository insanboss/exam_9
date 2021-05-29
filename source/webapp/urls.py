from django.urls import path, include

from webapp.views import IndexPhotos
from webapp.views.albums import AlbumView, AlbumCreate, AlbumDelete, AlbumUpdate
from webapp.views.favorites import AddPhoto, RemovePhoto, AddAlbum, RemoveAlbum
from webapp.views.photos import PhotoView, PhotoCreate, PhotoUpdate, PhotoDelete
from rest_framework import routers
from webapp import views


app_name = 'photos'

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)


favorites_urls = [
    path('<int:pk>/add_photo/', AddPhoto.as_view(), name='add_photo'),
    path('<int:pk>/remove_photo/', RemovePhoto.as_view(), name='remove_photo'),
    path('<int:pk>/add_album/', AddAlbum.as_view(), name='add_album'),
    path('<int:pk>/remove_album/', RemoveAlbum.as_view(), name='remove_album'),
]

urlpatterns = [
    path('', IndexPhotos.as_view(), name='index_photos'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreate.as_view(), name='photo_add'),
    path('photo/<int:pk>/update/', PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDelete.as_view(), name='photo_delete'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('album/create/', AlbumCreate.as_view(), name='album_create'),
    path('album/<int:pk>/delete/', AlbumDelete.as_view(), name='album_delete'),
    path('album/<int:pk>/update/', AlbumUpdate.as_view(), name='album_update'),
    path('favorites/', include(favorites_urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
