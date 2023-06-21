from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.utils import timezone

from .forms import *
from .utils import DataMixin

class ArticlesHome(DataMixin, ListView):
    model = Articles
    template_name = 'paper/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home", posts=self.get_queryset())
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Articles.objects.filter(is_published=True).select_related('category')

class ArticleCategory(DataMixin, ListView):
    model = Articles
    template_name = 'paper/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Articles.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'Category - {c.name}',
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, FormMixin, DetailView):
    model = Articles
    template_name = 'paper/post.html'
    slug_url_kwarg = "post_slug"
    context_object_name = "post"
    success_url = reverse_lazy('get_success_url')
    form_class = CommentsForm

    def get_success_url(self):
        url = self.get_object().slug
        return url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"], comments=Comments.objects.filter(article_id=self.get_object().id))
        return dict(list(context.items()) + list(c_def.items()))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save()
        self.object.article_id = self.get_object().id
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPageForm
    template_name = 'paper/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time = timezone.now()
        c_def = self.get_user_context(title="Add article", time=time)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not timezone.now() <= form.instance.publication_datetime:
            form.instance.is_published = True
        return super().form_valid(form)

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "paper/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аuthorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'paper/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class MyArticles(DataMixin, ListView):
    model = Articles
    template_name = 'paper/myarticles.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        c_def = self.get_user_context(title="My Articles", posts=self.get_queryset())
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Articles.objects.filter(user=self.request.user)


def logout_user(request):
    logout(request)
    return redirect("login")
