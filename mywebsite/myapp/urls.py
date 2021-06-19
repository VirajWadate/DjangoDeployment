from django.urls import path

from .views import index, fd, fd_calc

urlpatterns = [
    path('', index),
    path('fd', fd),
    path('fd_calc', fd_calc)
]