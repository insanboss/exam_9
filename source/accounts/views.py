from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import MyUserCreationForm, UserChangeForm, PasswordChangeForm


class RegisterView(CreateView):
    model = User
    template_name = 'registration/user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('photos:index_photos')
        return next_url


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        photos = self.get_object().photos_author.all()
        kwargs['photos'] = photos
        albums = self.get_object().album_author.all()
        kwargs['albums'] = albums
        return super().get_context_data(**kwargs)


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})
