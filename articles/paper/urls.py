from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('category/<slug:cat_slug>', ArticleCategory.as_view(), name='category'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('addarticle/', AddPage.as_view(), name='add_page'),
    path('myarticles/', MyArticles.as_view(), name='my_articles'),
]