from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(LoginRequiredMixin, DeleteView):
    template_name = 'albums/album_view.html'
    model = Album
    context_object_name = 'album'


class AlbumCreate(LoginRequiredMixin, CreateView):
    template_name = 'albums/album_create.html'
    model = Album
    form_class = AlbumForm

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author_album = self.request.user
        album.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photos:album_view', kwargs={'pk': self.object.pk})


class AlbumUpdate(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/album_update.html'
    form_class = AlbumForm
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def get_success_url(self):
        return reverse('photos:photo_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().album_author


class AlbumDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'albums/album_delete.html'
    model = Album
    context_object_name = 'album'
    permission_required = 'webapp.delete_album'
    success_url = reverse_lazy('photos:index_photos')

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().album_author
