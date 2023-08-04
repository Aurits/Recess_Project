from django.core.management.base import BaseCommand
from faker import Faker
from website.models import InstructorFeedback, CourseFeedback, FacilityFeedback, StudentDetails  # Update this line
import random 

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create dummy data for InstructorFeedback
        for _ in range(10):
            InstructorFeedback.objects.create(
                instructorName=fake.name(),
                department=fake.job(),
                courseUnit=fake.random_element(['Math', 'Physics', 'Chemistry', 'Biology']),
                knowledge=random.randint(20, 100),
                communication=random.randint(20, 100),
                teachingStyle=random.randint(20, 100),
                responsiveness=random.randint(20, 100),
                additional_comments=fake.paragraph()
            )

        # Create dummy data for CourseFeedback
        for _ in range(10):
            CourseFeedback.objects.create(
                courseName=fake.word(),
                courseCode=fake.random_number(digits=4),
                courseDescription=fake.paragraph(),
                effectiveness=random.randint(1, 5),
                interest=random.randint(1, 5),
                improvement=fake.paragraph()
            )

        # Create dummy data for FacilityFeedback
        for _ in range(10):
            FacilityFeedback.objects.create(
                name=fake.name(),
                facility_college=fake.random_element(['Engineering', 'Science', 'Arts', 'Business']),
                facility_accessibility=fake.random_element(['fully', 'partial', 'not']),
                cleanliness=fake.random_element(['very_good', 'good', 'fair', 'poor', 'very_poor']),
                maintenance=fake.random_element(['very_good', 'good', 'fair', 'poor', 'very_poor']),
                safety=fake.random_element(['very_good', 'good', 'fair', 'poor', 'very_poor']),
                resource_availability=fake.random_element(['very_good', 'good', 'fair', 'poor', 'very_poor']),
                facility_rating=fake.random_element(['very_good', 'good', 'fair', 'poor', 'very_poor']),
                comment=fake.paragraph()
            )

        # Create dummy data for StudentDetails
        for _ in range(10):
            StudentDetails.objects.create(
                name=fake.name(),
                studentId=fake.random_number(digits=7),
                emailAddress=fake.email(),
                year_of_study=fake.random_element(['Freshman', 'Sophomore', 'Junior', 'Senior'])
            )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data!'))
