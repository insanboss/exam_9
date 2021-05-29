from django.views.generic import DetailView

from webapp.models import Album


class AlbumView(DetailView):
    template_name = 'photos/album_view.html'
    model = Album
    context_object_name = 'album'
