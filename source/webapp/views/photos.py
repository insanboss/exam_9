from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo, Album, PhotoUser


class IndexPhotos(LoginRequiredMixin, ListView):
    template_name = 'photos/index_photos.html'
    context_object_name = 'photos'
    model = Photo
    queryset = Photo.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        photos_id = []
        for photo_id in PhotoUser.objects.filter(user=user):
            photos_id.append(photo_id.photo.pk)
        context['favorite_photos'] = photos_id

        return context


class PhotoView(LoginRequiredMixin,DetailView):
    template_name = 'photos/photo_view.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        photos_id = []
        for photo_id in PhotoUser.objects.filter(user=user):
            photos_id.append(photo_id.photo.pk)
        context['favorite_photos'] = photos_id

        return context


class PhotoCreate(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/photo_create.html'
    form_class = PhotoForm

    def get_success_url(self):
        return reverse(
            'photos:photo_view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        photo = form.save(commit=False)
        photo.album = album
        photo.author_photo = self.request.user
        photo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photos:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdate(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photos/photo_update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('photos:photo_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().photos_author


class PhotoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'photos/photo_delete.html'
    model = Photo
    context_object_name = 'photo'
    permission_required = 'webapp.delete_photo'
    success_url = reverse_lazy('photos:index_photos')

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().photos_author
