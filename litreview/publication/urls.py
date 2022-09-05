from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.TicketPage.as_view(), name='tickets'),
    path('tickets/<int:id>/edit',
         views.EditTicketPage.as_view(),
         name='edit_ticket')
]
