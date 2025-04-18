"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from tryon.views import try_on_clothes, try_on_clothes_page
from application.views import ApplicationCreate
from reviews.views import ReviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #review
    path('api/review/', ReviewView.as_view(), name='review'),


    #application
    path('api/create-application/', ApplicationCreate.as_view(), name='create-application'),

    #try on
    path('api/try-on/', try_on_clothes, name='try_on_clothes'),
    path('try-on-clothes/<int:shirt_id>/<int:pant_id>/', try_on_clothes_page, name='try_on_clothes_page'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
