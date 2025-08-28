from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, BookingForm
from .models import TravelOption, Booking, Profile
from django.db import transaction
from django.utils import timezone
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('travel_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def travel_list(request):
    qs = TravelOption.objects.all().order_by('date_time')
    qtype = request.GET.get('type')
    src = request.GET.get('source')
    dst = request.GET.get('destination')
    date = request.GET.get('date')
    if qtype:
        qs = qs.filter(type=qtype)
    if src:
        qs = qs.filter(source__icontains=src)
    if dst:
        qs = qs.filter(destination__icontains=dst)
    if date:
        qs = qs.filter(date_time__date=date)
    return render(request, 'travel_list.html', {'travels': qs})
@login_required
@transaction.atomic
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num_seats']
            if num <= 0:
                messages.error(request, 'Number of seats must be at least 1.')
            elif num > travel.available_seats:
                messages.error(request, 'Not enough available seats.')
            else:
                travel.available_seats -= num
                travel.save()
                total = travel.price * num
                booking = Booking.objects.create(
                    user=request.user,
                    travel_option=travel,
                    num_seats=num,
                    total_price=total,
                    booking_date=timezone.now(),
                    status='Confirmed'
                )
                messages.success(request, f'Booking confirmed (ID: {booking.id})')
                return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'book_travel.html', {'travel': travel, 'form': form})
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})
@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != 'Cancelled':
        booking.status = 'Cancelled'
        booking.travel_option.available_seats += booking.num_seats
        booking.travel_option.save()
        booking.save()
    return redirect('my_bookings')
@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'form': form})
