
from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('', include('todo.urls')),
    path('admin/', admin.site.urls),
    path('getElement/',views.getElement),
    path('postElement/',views.create_task)
]
