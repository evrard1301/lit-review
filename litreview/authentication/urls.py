from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.SignupPage.as_view(), name='signup')
]
