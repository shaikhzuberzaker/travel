from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking
from django.utils import timezone
class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.travel = TravelOption.objects.create(
            type='Bus', source='CityA', destination='CityB',
            date_time=timezone.now(), price=100.00, available_seats=10
        )
    def test_booking_creates_and_reduces_seats(self):
        self.client.login(username='testuser', password='pass')
        resp = self.client.post(f'/book/{self.travel.pk}/', {'num_seats': 2})
        self.assertEqual(resp.status_code, 302)
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 8)
        self.assertEqual(Booking.objects.count(), 1)
