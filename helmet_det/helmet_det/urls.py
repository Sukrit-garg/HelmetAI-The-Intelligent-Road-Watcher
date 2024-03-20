from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from helmetAI import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('result/',views.result,name="result")
] 
