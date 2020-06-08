from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.index, name="home"),

    path("about", views.about, name="about"),
    
    path("services", views.services, name="services"),

    path("ecommerce", views.ecommerce, name="ecommerce"),
    
    path("soft", views.soft, name="soft"),
    
    path("dm", views.dm, name="dm"),

    path("media", views.media, name="media"),
    
    path("contact", views.contact, name="contact"),
    
    
    
]
