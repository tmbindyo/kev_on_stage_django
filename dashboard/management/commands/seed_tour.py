from django.core.management.base import BaseCommand
from dashboard.models import Tour
from django.contrib.auth.models import User
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the Tour model with initial data'

    def handle(self, *args, **options):

        # Add your model-specific seed data here
        tour_data = [
            {
                'name': 'Polk Theater',
                'date': '2023-02-16',
                'time': '19:00:00',
                'location': 'Nashville, TN',
                'venue': 'Polk Theater',
                'link': 'https://cart.tpac.org/13379/13380',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'The Pageant',
                'date': '2023-02-17',
                'time': '19:00:00',
                'location': 'St. Louis, MO',
                'venue': 'The Pageant',
                'link': 'https://www.ticketmaster.com/event/06005F61913C55B0',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Flappers Comedy Club',
                'date': '2023-02-26',
                'time': '20:00:00',
                'location': 'Burbank, CA',
                'venue': 'Flappers Comedy Club',
                'link': 'https://www.flapperscomedy.com/shows/make-em-laugh-monday/72691/',
                'status_id': 1,
                'is_sold_out': True,
                'user_id': 1,
            },
            {
                'name': 'Riviera Theater',
                'date': '2023-03-01',
                'time': '18:30:00',
                'location': 'Chicago, IL',
                'venue': 'Riviera Theater',
                'link': 'https://www.axs.com/artists/1109532/kevonstage-tickets',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Bayou Music Hall',
                'date': '2023-03-09',
                'time': '19:30:00',
                'location': 'Houston, TX',
                'venue': 'Bayou Music Hall',
                'link': 'https://concerts.livenation.com/kevonstage-that-chick-angel-heres-the-houston-texas-03-09-2024/event/3A005F5ADD6D3502',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Majestic Theatre',
                'date': '2023-03-10',
                'time': '20:00:00',
                'location': 'Dallas, TX',
                'venue': 'Majestic Theatre',
                'link': 'https://www.axs.com/artists/1109532/kevonstage-tickets',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Lyric Theatre',
                'date': '2023-03-22',
                'time': '19:00:00',
                'location': 'Birmingham, AL',
                'venue': 'Lyric Theatre',
                'link': 'https://www.ticketmaster.com/event/20005F5ACC1910B0',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Coca Cola Roxy',
                'date': '2023-03-23',
                'time': '20:00:00',
                'location': 'Atlanta, GA',
                'venue': 'Coca Cola Roxy',
                'link': 'https://concerts.livenation.com/kevonstage-that-chick-angel-heres-the-atlanta-georgia-03-23-2024/event/0E005F59C1252BED',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Martin Marietta',
                'date': '2023-03-24',
                'time': '19:30:00',
                'location': 'Raleigh, NC',
                'venue': 'Martin Marietta',
                'link': 'https://www.ticketmaster.com/event/2D005F5BD2F578F7',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'Warner Theatre',
                'date': '2023-03-29',
                'time': '20:00:00',
                'location': 'Washington, DC',
                'venue': 'Warner Theatre',
                'link': 'https://concerts.livenation.com/kevonstage-the-chick-angel-heres-the-washington-district-of-columbia-03-29-2024/event/15005F5FA28816F2?_ga=2.232975582.1583657628.1698767999-1267034614.1697133054',
                'status_id': 1,
                'is_sold_out': True,
                'user_id': 1,
            },
            {
                'name': 'Miller Theater',
                'date': '2023-03-30',
                'time': '19:30:00',
                'location': 'Philadelphia, PA',
                'venue': 'Miller Theater',
                'link': 'https://www.ensembleartsphilly.org/events-and-tickets/2023-24/kcp/kevonstage/#close',
                'status_id': 1,
                'user_id': 1,
            },
            {
                'name': 'The Filmore Detroit',
                'date': '2023-03-31',
                'time': '20:00:00',
                'location': 'Detroit, MI',
                'venue': 'The Filmore Detroit',
                'link': 'https://concerts.livenation.com/kevonstage-that-chick-angel-heres-the-detroit-michigan-03-31-2024/event/08005F59CD942CE9',
                'status_id': 1,
                'user_id': 1,
            }

        ]

        # Seed the database
        for data in tour_data:
            # Check if the Tour record already exists
            if not Tour.objects.filter(name=data['name'], date=data['date'], time=data['time']).exists():
                # Convert date and time strings to datetime objects
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()
                data['time'] = datetime.strptime(data['time'], '%H:%M:%S').time()
                
                Tour.objects.create(**data)
                self.stdout.write(self.style.SUCCESS(f'Successfully seeded Tour model for {data["name"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Tour model for {data["name"]} already exists'))
