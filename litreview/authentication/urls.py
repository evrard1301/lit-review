from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('signup/', views.SignupPage.as_view(), name='signup')
]
