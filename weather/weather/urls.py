from django.contrib import admin
from django.urls import path
from the_weather import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),
]
