from django.contrib import admin
from .models import TravelOption, Booking, Profile
@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'source', 'destination', 'date_time', 'price', 'available_seats')
    list_filter = ('type', 'source', 'destination')
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'travel_option', 'num_seats', 'total_price', 'status', 'booking_date')
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city')
