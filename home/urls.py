from home.models import news
from django.urls import path

from . import views
from .views import NewsCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('', views.home , name='home-page'),
    path('base/', views.base , name='base-page'),
    path('course/', views.course , name='course-page'),
    path('about/', views.about , name='about-page'),
    path('vision/', views.vision , name='vision-page'),
    path('gallery/', views.gallery , name='gallery-page'),
    path('contact/', views.contact,name='contact'),
    

    path('cnews/',NewsCreateView.as_view(),name='news-create'),
    path('news/', views.NewsList,name='news-show'),
    path('news/<int:pk>/update/',views.NewsUpdateView.as_view(),name='news-update'),
    path('news/<int:pk>',views.NewsDetailView.as_view(),name='news-detail'),


    path('cach/',views.AchievementsCreateView.as_view(),name='achieve-create'),    
    path('achieve/', views.achListView.as_view(),name='achieve'),
    
    path('login/',auth_views.LoginView.as_view(template_name='home/login.html'),name='login'),   
    path('logout/',auth_views.LogoutView.as_view(template_name='home/logout.html'),name='logout'),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)