from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users if they don't exist
        user1, created1 = User.objects.get_or_create(username='john_doe', email='john@example.com', defaults={'password': 'password123'})
        user2, created2 = User.objects.get_or_create(username='jane_doe', email='jane@example.com', defaults={'password': 'password123'})

        # Create test teams if they don't exist
        team1, created_team = Team.objects.get_or_create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities if they don't exist
        Activity.objects.get_or_create(user=user1, activity_type='Running', defaults={'duration': timedelta(minutes=30)})
        Activity.objects.get_or_create(user=user2, activity_type='Cycling', defaults={'duration': timedelta(hours=1)})

        # Create test leaderboard entries if they don't exist
        Leaderboard.objects.get_or_create(user=user1, defaults={'score': 150})
        Leaderboard.objects.get_or_create(user=user2, defaults={'score': 200})

        # Create test workouts if they don't exist
        Workout.objects.get_or_create(name='Push-ups', defaults={'description': 'Do 20 push-ups'})
        Workout.objects.get_or_create(name='Sit-ups', defaults={'description': 'Do 30 sit-ups'})

        # Add a log message to confirm test data creation
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data for users, activities, and workouts'))