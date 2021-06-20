from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .models import Post

# Вьюшка детальной информации поста а также отображения комментариев
"""Добавлен форм миксин для передачи формы комментариев"""


class ArticleDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'detail_article.html'
    form_class = CommentForm
    context_object_name = 'get_article'

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


# Вьюшка списка постов на главной странице
class ArticleListView(ListView):
    model = Post
    template_name = 'test3/index.html'
    context_object_name = 'get_article'


# Вьюшка создания постов
class ArticleCreateView(CreateView):
    model = Post
    template_name = 'create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('home')


# Вьюшка редактирования постов
class ArticleUpdateView(UpdateView):
    model = Post
    template_name = "edit_page.html"
    form_class = ArticleForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


# Вьюшка под логин
class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


# Вьюшка регистрации нового пользователя
class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


# Вьюшка выхода
class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')


# Вьюшка для удаления
class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'test3/index.html'
    success_url = reverse_lazy('home')
