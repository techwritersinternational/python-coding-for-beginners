from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import handler404, handler500
from samples import error_views

urlpatterns = [
    path('', views.sample_list, name='sample_list'),
    path('sample/<int:pk>/', views.sample_detail, name='sample_detail'),
    path('sample/new/', views.sample_create, name='sample_create'),
    path('sample/<int:pk>/edit/', views.sample_update, name='sample_update'),
    path('sample/<pk>/delete/', views.sample_delete, name='sample_delete'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]

handler404 = error_views.handler404
handler500 = error_views.handler500