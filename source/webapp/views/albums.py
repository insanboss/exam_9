from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(DetailView):
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


class AlbumDelete(LoginRequiredMixin, DeleteView):
    template_name = 'albums/album_delete.html'
    model = Album
    context_object_name = 'album'

    success_url = reverse_lazy('photos:index_photos')
