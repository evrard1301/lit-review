from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.TicketPage.as_view(), name='tickets')
]
