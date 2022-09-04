from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('signup/', views.SignupPage.as_view(), name='signup')
]
