from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="image"),
    path('gallery/', views.gallery_view, name="gallery"),
]
