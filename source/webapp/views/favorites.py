from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from webapp.models import Photo, PhotoUser, Album, AlbumUser


class AddPhoto(View):
    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            PhotoUser.objects.get(photo=photo, user=user)
            return HttpResponseForbidden('you already add that')
        except PhotoUser.DoesNotExist:
            PhotoUser.objects.create(photo=photo, user=user)
            return HttpResponse(photo.PhotoUser.count())


class RemovePhoto(View):
    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            favorite = PhotoUser.objects.get(photo=photo, user=user)
            favorite.delete()
            return HttpResponse(photo.PhotoUser.count())
        except PhotoUser.DoesNotExist:
            return HttpResponseForbidden('you already removed that')


class AddAlbum(View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            AlbumUser.objects.get(album=album, user=user)
            return HttpResponseForbidden('you already add that')
        except AlbumUser.DoesNotExist:
            AlbumUser.objects.create(album=album, user=user)
            return HttpResponse(album.AlbumUser.count())


class RemoveAlbum(View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            favorite_album = AlbumUser.objects.get(album=album, user=user)
            favorite_album.delete()
            return HttpResponse(album.AlbumUser.count())
        except AlbumUser.DoesNotExist:
            return HttpResponseForbidden('You already removed that')


