from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.TicketPage.as_view(), name='tickets'),
    path('tickets/<int:id>/edit',
         views.EditTicketPage.as_view(),
         name='edit_ticket'),
    path('tickets/<int:id>/delete',
         views.DeleteTicket.as_view(),
         name='delete_ticket'),
    path('tickets/<int:id>/review',
         views.CreateTicketReview.as_view(),
         name='ticket_review'),
    path('tickets/review',
         views.CreateFullReview.as_view(),
         name='full_review'),
    path('reviews/<int:id>/edit',
         views.EditReview.as_view(),
         name='edit_review'),
    path('reviews/<int:id>/delete',
         views.DeleteReview.as_view(),
         name='delete_review')
]
