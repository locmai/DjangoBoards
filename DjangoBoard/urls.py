"""DjangoBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boards import views as board_views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board_views.home, name='home'),
    path('boards/<int:board_id>/', board_views.board_topics, name='board_topics'),
    path('boards/<int:board_id>/new/', board_views.new_topic, name='new_topic'),
    path('signup/', account_views.sign_up, name='sign_up'),
    path('logout/',auth_views.LogoutView.as_view(), name='log_out'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='log_in'),
]
