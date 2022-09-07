from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.MePage.as_view(), name='me')
]
