import random
from django.core.management.base import BaseCommand
from visitors.models import Visitor, User

class Command(BaseCommand):
    help = 'Create dummy visitors, staff, and contract users'

    def handle(self, *args, **kwargs):
        # Create dummy users
        users = []
        for i in range(5):
            users.append(User.objects.create_user(
                email=f'user{i}@example.com',
                password='password123',
                first_name=f'User{i}',
                last_name=f'Surname{i}'
            ))

        # Create dummy visitors
        visitor_types = ['Visitor', 'Staff', 'Contractor']
        
        for i in range(10):
            Visitor.objects.create(
                first_name=f'Visitor{i}',
                last_name=f'Surname{i}',
                email=f'visitor{i}@example.com',
                sign_in_time=f'2024-06-11 12:00:00',
                visitor_type=random.choice(visitor_types),
                
            )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data'))
