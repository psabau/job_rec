# main/urls.py

from django.urls import path
from . import views
from .views import home_view, login_view, SignUpView, CustomLoginView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
