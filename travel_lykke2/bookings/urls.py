from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('travels/', views.travel_list, name='travel_list'),
    path('book/<int:pk>/', views.book_travel, name='book_travel'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile_edit, name='profile_edit'),
]
