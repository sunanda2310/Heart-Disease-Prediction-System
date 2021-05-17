"""heartDiseasePrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static



#custom pages
from pages.views import home_view, contact_view,change_password_view, user_heart_info_view, about_view, footer_view, prediction_page_view, login_view, header_view, login_validation_view, registration_view, profile_view, user_info_view, login_failure_view, user_heart_info_save_view, user_heart_info_save_display_view, change_password_view_record

urlpatterns = [
    #create diff pages and route that here like contact etc
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('userInfo/', user_heart_info_view, name='userInfo'),
    path('about/', about_view, name='about'),
    path('footer/', footer_view, name='footer'),
    path('prediction/', prediction_page_view, name='prediction'),
    path('login/', login_view, name='login'),
    path('loginValidation/', login_validation_view, name='loginValidation'),
    path('register/', registration_view, name='register'),
    path('header/', header_view, name='header'),
    path('profile/', profile_view, name='profile'),
    path('userDetails/', user_info_view, name='userDetails'),
    path('loginFailure/', login_failure_view, name='loginFailure'),
    path('userHeartInfoSave/', user_heart_info_save_view, name='userHeartInfoSave'),
    path('userHeartInfoSaveDisplay/', user_heart_info_save_display_view, name='userHeartInfoSaveDisplay'),
    path('admin/', admin.site.urls),
    path('change_password/', change_password_view, name='change_password'),
    path('change_password_success_page/', change_password_view_record, name='change_password_success_page'), 
]



