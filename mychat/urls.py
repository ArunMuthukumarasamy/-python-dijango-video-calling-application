from django.contrib import admin
from django.urls import path , include
from base.views import signup , frontpage


urlpatterns = [
    path('', include('base.urls')),
    path('chatrooms/',include('chatroom.urls')),
    
    path('admin/', admin.site.urls),
   

    
   
]

